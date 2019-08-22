from pyexpat.errors import messages

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import SiteUserCreationForm
from users.models import SiteUser


@login_required(login_url='/auth/login')
def profile(request, user_id):
    if user_id is not request.user.id:
        messages.error(request, 'You do not have permission to view this profile.')
        return redirect('/reports/')
    return render(request, 'registration/account.html')


class SignUp(CreateView):
    form_class = SiteUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
