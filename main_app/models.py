from django.db import models
from django.urls import reverse

# Create your models here.


class Record(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    # artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'record_id': self.id})


class Artist(models.Model):
    name = models.CharField(max_length=100)
    members = models.TextField(max_length=250)
    # record = models.ForeignKey(Record, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# add format model
