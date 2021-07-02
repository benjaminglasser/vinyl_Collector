from django.shortcuts import render
from .models import Vinyl


# vinyl = [
#     Vinyl('The Rolling Stones', 'Some Girls', 1978, 'Rock'),
#     Vinyl('Nas', 'Illmatic', 1994, 'Hip-Hop'),
#     Vinyl('The Flaming Lips', 'The Soft Bulletin', 1999, 'Alternative/Indie'),
#     Vinyl('Floating Points', 'Crush', 2019, 'Electronic'),
# ]


# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def vinyl_index(request):
    vinyl = Vinyl.objects.all()
    return render(request, 'vinyl/index.html', {'vinyl': vinyl})
