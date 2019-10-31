from pyexpat.errors import messages

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from cr_dynamic import settings
from reports.models import Interaction
from users.forms import SiteUserCreationForm
from users.models import SiteUser


@login_required(login_url='/auth/login')
def profile(request, user_id):
    if user_id is not request.user.id:
        messages.error(request, 'You do not have permission to view this profile.')
        return redirect('/reports/')
    return render(request, 'registration/account.html')


@login_required(login_url='/auth/login')
def interactions(request, user_id):
    if user_id is not request.user.id:
        messages.error(request, 'You do not have permission to view this page.')
        return redirect('/reports/')
    interaction_list = Interaction.objects.all().filter(user=SiteUser.objects.get(id=user_id)).order_by('-timestamp')[:25]
    context = {'interaction_list': interaction_list}

    return render(request, 'registration/interactions.html', context)


def custom_login(request, **kwargs):
    if request.user.is_authenticated():
        messages.error(request, 'You are already logged in.')
        return redirect('/')
    else:
        return login(request, kwargs)

class SignUp(CreateView):
    form_class = SiteUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def enabled(self, request, *args, **kwargs):
        if not settings.ALLOW_NEW_USERS:
            messages.error(self.request, 'New user registration is currently closed.')
            return redirect('/auth/login')
