from django.contrib.auth import get_user_model  
from rest_framework import serializers  

User = get_user_model()  # Fetch the custom user model  

class UserSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = User  
        fields = ['id', 'username', 'email', 'name', 'image', 'online', 'groups'] 