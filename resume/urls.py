from django.urls import path  
from .views import Home, UserLogin, UserLogout, AdminChat, ContactUs, ConnectionToAdmin, SendMassage

urlpatterns = [  
    # pages
    path('', Home, name='Home'),
    path('AdminChat/', AdminChat, name='AdminChat'), 
    path('UserLogout/', UserLogout, name='UserLogout'),
    path('UserLogin/', UserLogin, name='UserLogin'),  
    path('ContactUs/', ContactUs, name='ContactUs'),  
    # connection
    path('ConnectionToAdmin/', ConnectionToAdmin, name='ConnectionToAdmin'), 
    # send massages
    path('SendMassage/', SendMassage, name='SendMassage'), 
]  
