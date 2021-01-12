from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'profiles'
urlpatterns = [
    path('', views.profile, name='profile'),
    path('band-creation/', views.band_creation, name='band-creation'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)