from django.urls import path  
from .views import home, ADMIN_CHAT  

urlpatterns = [  
    path('', home, name='home'), 
    path('contact/', ADMIN_CHAT, name='ADMIN_CHAT'), 
]