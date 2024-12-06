from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "home.html")

def ADMIN_CHAT(request):
    return render(request,'chat.html')