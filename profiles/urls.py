from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'profiles'
urlpatterns = [
    path('', views.profile, name='profile'),
    path('band-creation/', views.band_creation, name='band-creation'),
    path('edit-band/<str:id>/', views.edit_band, name='edit-band'),
]
    