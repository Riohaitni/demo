from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *



from django.contrib import admin
from .models import  Friendship, FriendRequest, FriendInvitation


admin.site.register([FriendRequest])
admin.site.register([FriendInvitation])
admin.site.register([Friendship])


