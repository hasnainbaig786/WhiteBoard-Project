# from django.contrib import admin
# from .models import *
# # Register your models here.

# admin.site.register(Name, email, _Password)



from django.contrib import admin
from .models import *

# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email' ,'password')
    # You can customize the admin options here

admin.site.register(Name)
# , UserProfileAdmin
