from django.urls import path, include  
from .views import Home, UserLogin, UserLogout, AdminChat, ContactUs, ConnectionToAdmin, SendMassage, UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [  
    # pages
    path('', include(router.urls)),
    path('home/', Home, name='Home'),
    path('AdminChat/', AdminChat, name='AdminChat'), 
    path('UserLogout/', UserLogout, name='UserLogout'),
    path('UserLogin/', UserLogin, name='UserLogin'),  
    path('ContactUs/', ContactUs, name='ContactUs'),  
    # connection
    path('ConnectionToAdmin/', ConnectionToAdmin, name='ConnectionToAdmin'), 
    # send massages
    path('SendMassage/', SendMassage, name='SendMassage'), 
]  
