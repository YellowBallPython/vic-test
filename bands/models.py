from django.db import models
from django.contrib.auth.models import User

class Band(models.Model):
    name = models.CharField(max_length=200, verbose_name='nombre')
    img = models.ImageField(verbose_name='foto', upload_to='bands_pics', default='default-band.png')
    genre = models.CharField(max_length=200, verbose_name='género')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name