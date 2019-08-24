from pyexpat.errors import messages

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

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


class SignUp(CreateView):
    form_class = SiteUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
