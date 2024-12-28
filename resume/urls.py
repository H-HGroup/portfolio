from django.urls import path, include  
from . import views
from rest_framework import routers



urlpatterns = [  
    # pages
    path('', views.Home, name='Home'),
    path('AdminChat/', views.AdminChat, name='AdminChat'), 
    path('UserLogout/', views.UserLogout, name='UserLogout'),
    path('UserLogin/', views.UserLogin, name='UserLogin'),  
    path('ContactUs/', views.ContactUs, name='ContactUs'),  
    path('Projects/', views.ProjectsApiView.as_view(), name='Projects'),  
    path('Experience/', views.ExperienceApiView.as_view(), name='Experience'),  
    path('Education/', views.EducationApiView.as_view(), name='Education'),  


    # connection
    path('ConnectionToAdmin/', views.ConnectionToAdmin, name='ConnectionToAdmin'), 
    # send massages
    path('SendMassage/', views.SendMassage, name='SendMassage') 
]  
