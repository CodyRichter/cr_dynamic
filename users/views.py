from pyexpat.errors import messages

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required(login_url='/auth/login')
def profile(request, user_id):
    if user_id is not request.user.id:
        messages.error(request, 'You do not have permission to view this profile.')
        return redirect('/reports/')
    return render(request, 'registration/account.html')
