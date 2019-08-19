from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new, name='new'),
    path('<int:post_id>/edit', views.edit, name='edit'),
    path('<int:post_id>/delete', views.delete, name='delete'),
    path('<int:post_id>/', views.detail, name='detail'),
]
