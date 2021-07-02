from django.db import models

# Create your models here.


class Vinyl(models.Model):
    artist = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.artist
