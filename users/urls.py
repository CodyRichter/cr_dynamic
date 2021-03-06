from django.urls import path

from . import views

urlpatterns = [
    path('<int:user_id>', views.profile, name='profile'),
    path('<int:user_id>/interactions/', views.interactions, name='interactions'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]
