from django.contrib import admin
from .models import Users

# Register your models here.

admin.site.register(Users)

class My_User(admin.ModelAdmin):
    list_display=['name','email','password']
