# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

from .models import SiteUser


class SiteUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = SiteUser
        fields = ('username', 'email',)


class SiteUserChangeForm(UserChangeForm):

    class Meta:
        model = SiteUser
        fields = ('username', 'email',)

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
