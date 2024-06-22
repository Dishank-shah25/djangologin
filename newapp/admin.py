from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User
class showuser(admin.ModelAdmin):  
    list_display = ['username','password','email']
admin.site.register(User,showuser)

