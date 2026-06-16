from django.contrib import admin
from .models import User, InvitationCode

# admin.site.register(User) we using custom user abstractuser 
admin.site.register(InvitationCode)