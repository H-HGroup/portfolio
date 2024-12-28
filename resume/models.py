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


class Education(models.Model):
    school = models.CharField(max_length=100)
    years = models.CharField(max_length=50)
    univercity = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    descrption = models.TextField()
    order = models.IntegerField(default=1)


class Experience(models.Model):
    title = models.CharField(max_length=50)
    descrption = models.TextField()
    years = models.CharField(max_length=50)
    order = models.IntegerField(default=1)


class Projects(models.Model):
    title = models.CharField(max_length=50)
    descrption = models.TextField()
    image = models.ImageField(upload_to='images_uploaded', null=True, blank=True)
    url = models.URLField(max_length=200)
    order = models.IntegerField(default=1)

