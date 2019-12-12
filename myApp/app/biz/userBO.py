from app.biz.UserResult import *
from app.models import Users
from app.biz.classificationBO import ClassificationBO
import json
class UserBO:
    classificationBO=ClassificationBO()
    def Control(self,userResult:UserResult):
        dbUser = Users.objects.filter(height=userResult.height, weight=userResult.weight, shoeSize=userResult.shoeSize)
        user = str(userResult.height) + " " + str(userResult.weight) + " " + str(userResult.shoeSize)

        gender = self.classificationBO.Bul(userResult)
        userResult.gender=gender
        if user in str(dbUser):
            message = "\n Verileriniz Kayıtlı."
        else:
            Users.objects.create(height=userResult.height, weight=userResult.weight, shoeSize=userResult.shoeSize, gender=userResult.gender[0])
            message = "\n Sağlıklı Sonuçlar Elde Etmek İçin Verileriniz Kayıt Edildi."

        userResult.message=message
        userResult.jsonResult=json.dumps({
            'boy': userResult.height,
            'kilo': userResult.weight,
            'ayakkabi numarasi': userResult.shoeSize,
            'cinsiyet': userResult.gender,
            'mesaj':userResult.message})

        return userResult