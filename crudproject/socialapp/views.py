from django.http import JsonResponse
from django.shortcuts import redirect, render
from . models import *


def signup(request):
    if request.method=='POST':
        name=request.POST['name']
        username=request.POST['username']
        password=request.POST['password']
        confirmpassword=request.POST['password']
        details=Signup(name=name,username=username,password=password,confirmpassword=confirmpassword)
        details.save()
        return redirect("signuptable")
    return render(request,'signup.html')


def signuptable(request):
     infodetails=Signup.objects.all()
     return render(request, 'signuptable.html')



def login(request):
     if request.method=='POST':
          username=request.POST['username']
          password=request.POST['password']
          try:
               current_user=Signup.objects.get(username=username,password=password)
               request.session['xyz']=current_user.id
               return redirect("signuptable")
          except Signup.DoesNotExist:
               return render(request,'login.html',{"message":"username password wrong"})
     return render(request,'login.html') 
