from django.forms import ModelForm
from .models import Artist, Format


class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'members']


class FormatForm(ModelForm):
    class Meta:
        model = Format
        fields = ['format']
