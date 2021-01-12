from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pic = models.ImageField(verbose_name='profile pic',
                            upload_to='profile_pics',
                            default='default-profile.jpg'
                            )

    def __str__(self):
        return f'{self.user} Profile'
