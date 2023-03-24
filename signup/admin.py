from django.contrib import admin
from signup.models import User

class UserAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','sex','email','password')

admin.site.register(User,UserAdmin)