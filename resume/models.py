from django.db import models

# Create your models here.

class Connection(models.Model):
    userName = models.CharField(max_length=50, null=True, blank=True)
    userNumber = models.CharField(max_length=10, blank=True, null=True)
    admin = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f'{self.userName} connected to {self.admin}'