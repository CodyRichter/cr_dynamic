from pyexpat.errors import messages

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import SiteUserCreationForm


@login_required(login_url='/auth/login')
def profile(request, user_id):
    if user_id is not request.user.id:
        messages.error(request, 'You do not have permission to view this profile.')
        return redirect('/reports/')
    return render(request, 'registration/account.html')


@login_required(login_url='/auth/login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/auth/' + str(request.user.id))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {'form': form})


class SignUp(CreateView):
    form_class = SiteUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
