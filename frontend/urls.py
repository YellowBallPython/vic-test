from django.urls import path
from django.contrib.auth import views as auth_views
from profiles import views as profiles_views
from . import views

app_name = 'frontend'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.index, name='contact'),
    path('login/', auth_views.LoginView.as_view(template_name='profiles/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='profiles/logout.html'), name='logout'),
    path('register/', profiles_views.register, name='register'),
]
