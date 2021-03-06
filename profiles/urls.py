from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'profiles'
urlpatterns = [
    path('', views.profile, name='profile'),
    path('bands', views.band_list, name='band-list'),
    path('band-creation/', views.band_creation, name='band-creation'),
    path('edit-band/<str:id>/', views.edit_band, name='edit-band'),
    path('delete-band/<str:id>/', views.delete_band, name='delete-band'),
]
    