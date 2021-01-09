from django.urls import path
from . import views


app_name = 'reservations'
urlpatterns = [
    path('', views.lista, name='lista'),
    path('make/', views.make_res, name='make'),
    path('success/', views.success, name='success'),
]
