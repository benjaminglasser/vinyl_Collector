from django.db import models
from django.urls import reverse


FORMATS = (
    ('V', 'Vinyl'),
    ('C', 'CD'),
    ('T', 'Cassette'),
    ('D', 'Digital')
)


class Artist(models.Model):
    name = models.CharField(max_length=100)
    members = models.TextField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('artist_detail', kwargs={'pk': self.id})


class Record(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    artists = models.ManyToManyField(Artist)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'record_id': self.id})

# format model


class Format(models.Model):
    format = models.CharField(
        max_length=1,
        choices=FORMATS,
        default=FORMATS[0][0]
    )
    record = models.ForeignKey(Record, on_delete=models.CASCADE)

    def __str__(self):
        return {self.get_format_display()}
