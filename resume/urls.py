from django.urls import path  
from .views import Home, UserLogin, UserLogout, AdminChat, ContactUs, ConnectionToAdmin

urlpatterns = [  
    path('', Home, name='Home'),
    path('AdminChat/', AdminChat, name='AdminChat'), 
    path('UserLogout/', UserLogout, name='UserLogout'),
    path('UserLogin/', UserLogin, name='UserLogin'),  
    path('ContactUs/', ContactUs, name='ContactUs'),  
    path('ConnectionToAdmin/', ConnectionToAdmin, name='ConnectionToAdmin'), 
]  
