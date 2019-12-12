from sklearn import tree
import mysql.connector

from app.biz.UserResult import UserResult
from .classificationDTO import *
class ClassificationBO(ClassificationDTO):
    def Bul(self,userResult:UserResult):
        test_data = [[userResult.height,userResult.weight,userResult.shoeSize]]
        dbContext = mysql.connector.connect(user="dbDiyetAdmin", password="297862", host="localhost", database="dbCinsiyet")
        cursor = dbContext.cursor()

        dbQuery = ("SELECT height,weight,shoeSize FROM app_users")
        cursor.execute(dbQuery)
        sonuc = cursor.fetchall()


        for x in sonuc:
            height = x[0]
            weight = x[1]
            shoeSize = x[2]
            Z = [height, weight, shoeSize]
            ClassificationDTO.X.append(Z)

        dbQuery = ("SELECT gender FROM app_users ")
        cursor.execute(dbQuery)
        sonuc = cursor.fetchall()

        for x in sonuc:
            gender = x[0]
            ClassificationDTO.Y.append(gender)

        dtc_clf = tree.DecisionTreeClassifier()
        dtc_clf = dtc_clf.fit(ClassificationDTO.X,ClassificationDTO.Y)
        dtc_prediction = dtc_clf.predict(test_data)

        return dtc_prediction[0]

