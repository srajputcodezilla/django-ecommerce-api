from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ["username","email","user_id","ifLogged"]
admin.site.register(User, UserAdmin)