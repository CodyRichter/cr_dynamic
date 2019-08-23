from django.contrib.auth.views import PasswordChangeView
from django.urls import path

from . import views

urlpatterns = [
    path('<int:user_id>', views.profile, name='profile'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]
