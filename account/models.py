from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    name = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='images_uploaded', null=True, blank=True)
    online = models.BooleanField(default=False)


