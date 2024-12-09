from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from .forms import *

def Home(request):
    return render(request, "home.html")

def AdminChat(request):
    return render(request,'chat.html')





def UserLogout(request):  
    logout(request)  
    return redirect('Home')  

def UserLogin(request):  
    if request.method == 'POST':  
        form = UserLoginForm(request.POST)  
        if form.is_valid():  
            data = form.cleaned_data  
            user = authenticate(request, username=data['username'], password=data['password'])  

            if user is not None:  
                login(request, user)  
                return redirect('AdminChat')
  

