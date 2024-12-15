from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

UserAdmin.fieldsets += (('Other Fields', {'fields':('name', 'image', 'online')}),)

admin.site.register(User, UserAdmin)