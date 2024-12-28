from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserLoginForm  
from .models import Connection, Education, Experience, Projects, Masseges
from account.models import User
import json
from django.http import JsonResponse
import random
from rest_framework import permissions, viewsets
from .serializers import UserSerializer, EducationSerializer, ExperienceSerializer, ProjectsSerializer
from django.contrib.auth import get_user_model  
from rest_framework import viewsets, permissions  
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt  
import logging


User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):  
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer  
    permission_classes = [permissions.IsAuthenticated] 


# link pages

def Home(request):
    return render(request, "home.html")


def AdminChat(request):
    return render(request,'chat.html')

def ContactUs(request):
    return render(request, 'contact.html')


class ProjectsApiView(generics.ListAPIView):
    queryset = Projects.objects.order_by('order').all()
    serializer_class = ProjectsSerializer
    
class EducationApiView(generics.ListAPIView):
    queryset = Education.objects.order_by('order').all()
    serializer_class = EducationSerializer

class ExperienceApiView(generics.ListAPIView):
    queryset = Experience.objects.order_by('order').all()
    serializer_class = ExperienceSerializer
    

#  user logout

def UserLogout(request):  
    logout(request)  
    return redirect('Home')  



# user login 

def UserLogin(request):  
    if request.method == 'POST':  
        form = UserLoginForm(request.POST)  
        if form.is_valid():  
            data = form.cleaned_data  
            user = authenticate(request, username=data['username'], password=data['password'])  

            if user is not None:  
                login(request, user)  
                if user.is_superuser:  
                    return redirect('AdminChat')  
                else:  
                    return redirect('Home')   

        return render(request, 'home.html', {'form': form, 'error': 'نام کاربری یا رمز عبور نامعتبر است'})   

    else:  
        form = UserLoginForm()  
        return render(request, 'home.html', {'form': form})




#  connect customer to admin

def ConnectionToAdmin(request):
    data = json.loads(request.body)
    hasRecord = Connection.objects.filter(userName = data['userName'], userNumber = data['userNumber']).exists()

    admin = User.objects.filter(is_staff = True, online = True)
    if(len(admin)>1):
        admin = admin[random.randint(0, len(admin)-1)]
    elif(len(admin)==1):
        admin = admin[0]
    else:
        admin = 'offline'


    if hasRecord:
        Connection.objects.filter(userName = data['userName'], userNumber = data['userNumber']).delete()
        Connection.objects.create(userName = data['userName'], userNumber = data['userNumber'], admin = admin)
        return JsonResponse({'connection status':'delet and connect', 'admin':str(admin)})
    else:
        Connection.objects.create(userName = data['userName'], userNumber = data['userNumber'], admin = admin)
        return JsonResponse({'connection status':'connect', 'admin':str(admin)})



#  send massage from customer to admin

  

logger = logging.getLogger(__name__)  


def SendMassage(request):  
    if request.method == 'POST':  
        try:  
            logger.info(f'Received body: {request.body}')  
            data = json.loads(request.body)  

            required_fields = ['msg', 'senderName', 'senderNumber', 'reciver']  
            for field in required_fields:  
                if field not in data:  
                    return JsonResponse({'error': f'Missing field: {field}'}, status=400)  

            save_massage = Masseges.objects.create(  
                massegeText=data['msg'],  
                senderName=data['senderName'],  
                senderNumber=data['senderNumber'], 
                reciver=data['reciver']  
            )  

            return JsonResponse({  
                'massage': save_massage.massegeText,  
                'senderName': save_massage.senderName,  
                'reciver': save_massage.reciver,  
                'time': save_massage.creat.time()  
            }, safe=True)  

        except json.JSONDecodeError:  
            return JsonResponse({'error': 'Invalid JSON'}, status=400)  
        except Exception as e:  
            logger.error(f'Error saving message: {e}')  
            return JsonResponse({'error': 'Internal Server Error'}, status=500)  
    else:  
        return JsonResponse({'error': 'Invalid request method'}, status=405)