from django.shortcuts import render, HttpResponse, redirect
from app.forms import UserForm
from app.biz.userBO import UserBO
from django.contrib import messages
from app.biz.UserResult import *
from django.views.decorators.csrf import csrf_exempt
import json

def create(request):
    form=UserForm(request.POST)
    userBO=UserBO()
    userResult=UserResult()
    if request.method=="POST":
       if form.is_valid():
            form = UserForm(request.POST)
            userResult.height = request.POST.get('height')
            userResult.weight = request.POST.get('weight')
            userResult.shoeSize = request.POST.get('shoeSize')
            userResult=userBO.Control(userResult)
            return HttpResponse(userResult.jsonResult, content_type="application/json")
    else:
        form=UserForm()
    return render(request,'app/index.html',{'form':form})

@csrf_exempt
def createAPI(request):
    userBO=UserBO()
    userResult=UserResult()
    if request.method=="POST":
        userResult.height = request.POST.get('height')
        userResult.weight = request.POST.get('weight')
        userResult.shoeSize = request.POST.get('shoeSize')
        userResult=userBO.Control(userResult)

    else:
        userResult.message="GEÇERSİZ FORM İSTEĞİ"
        userResult.jsonResult = json.dumps({
            'boy': None,
            'kilo': None,
            'ayakkabi numarasi': None,
            'cinsiyet': None,
            'mesaj': userResult.message,
            'request':request.method
        })
    return HttpResponse(userResult.jsonResult, content_type="application/json")

def readJsonFile(request):
    jsonResult=open('user.json','r').read()
