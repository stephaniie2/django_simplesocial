#GROUPS admin.py
from django.contrib import admin
from . import models

class GroupMemberInline(admin.TabularInLine):
    model = models.GroupMember

admin.site.register(models.Group)
