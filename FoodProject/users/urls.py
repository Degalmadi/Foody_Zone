from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.users_home, name='home'),   # handles /users/
    path('register/', views.register, name='reg'),
    path('profile/', views.profile, name='profile'),
]