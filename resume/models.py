from django.db import models
from django.utils import timezone

# Create your models here.

class Connection(models.Model):
    userName = models.CharField(max_length=50, null=True, blank=True)
    userNumber = models.CharField(max_length=10, blank=True, null=True)
    admin = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f'{self.userName} connected to {self.admin}'
    

class Masseges(models.Model):
    massegeText = models.TextField()
    senderName = models.CharField(max_length=50)
    senderNumber = models.CharField(max_length=50)
    reciver = models.CharField(max_length=50)
    received = models.BooleanField(default=False)
    creat = models.DateTimeField(auto_now_add=True)
    creat = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"from {self.senderName} to {self.reciver} ====> {self.massegeText}"
