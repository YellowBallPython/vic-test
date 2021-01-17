from django.urls import path
from . import views


app_name = 'reservations'
urlpatterns = [
    path('', views.reservations_list, name='lista'),
    path('make/', views.make_res, name='make'),
    path('success/', views.success, name='success'),
    path('my-res/', views.my_res, name='my-res'),
]
