from django.db import models

class Users(models.Model):
    height = models.IntegerField()
    weight = models.IntegerField()
    shoeSize = models.IntegerField()
    gender=models.CharField(max_length=10,default="Null")
    def __str__(self):
        return str(self.height)+" "+str(self.weight)+" "+str(self.shoeSize)
