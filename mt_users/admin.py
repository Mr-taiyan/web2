from django.contrib import admin
from models import *

class User_info_admin(admin.ModelAdmin):
    list_display = ['name','email','paid']
    search_fields = ['name','email']
    list_per_page = 20

admin.site.register(User_info,User_info_admin)
