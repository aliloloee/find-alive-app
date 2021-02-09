from django.contrib import admin
from .models import MyUser


class MyUserAdmin(admin.ModelAdmin) :
    model = MyUser
    list_display = ('email', 'user_name', 'id', 'is_active', 'is_staff')

admin.site.register(MyUser, MyUserAdmin)
