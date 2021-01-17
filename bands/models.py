from django.db import models
from django.contrib.auth.models import User

class Band(models.Model):
    name = models.CharField(max_length=200, verbose_name='nombre')
    img = models.ImageField(verbose_name='foto', upload_to='bands_pics', default='default-band.jpg', null=True, blank=True)
    genre = models.CharField(max_length=200, verbose_name='género', blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} de {self.owner}_id: {self.owner.id}'