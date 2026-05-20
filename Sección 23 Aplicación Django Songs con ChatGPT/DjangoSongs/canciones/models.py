from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Cancion(models.Model):
    titulo = models.CharField(max_length=255)
    artista = models.CharField(max_length=255)
    popularidad = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )

    def __str__(self):
        return f"{self.titulo} - {self.artista}"

    class Meta:
        db_table = 'cancion'
        verbose_name = 'Canción'
        verbose_name_plural = 'Canciones'

