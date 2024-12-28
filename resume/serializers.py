from django.contrib.auth import get_user_model  
from rest_framework import serializers  
from . import models

User = get_user_model()  # Fetch the custom user model  

class UserSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = User  
        fields = ['id', 'username', 'email', 'name', 'image', 'online', 'groups'] 


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Education
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Experience
        fields = '__all__'

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Projects
        fields = '__all__'
