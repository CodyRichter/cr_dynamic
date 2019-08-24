# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from reports.models import Interaction
from .forms import SiteUserChangeForm, SiteUserCreationForm
from .models import SiteUser


class SiteUserAdmin(UserAdmin):
    add_form = SiteUserCreationForm
    form = SiteUserChangeForm
    model = SiteUser
    list_display = ['email', 'username', ]
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('role',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('role',)}),)


admin.site.register(SiteUser, SiteUserAdmin)
