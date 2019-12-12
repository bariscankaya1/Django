from rest_framework import serializers

from .models import *

class UsersSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Users
        fields = ['id','height','weight','shoeSize','gender']