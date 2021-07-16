from django.shortcuts import render
from .models import Record


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


def record_index(request):
    record = Record.objects.all()
    return render(request, 'record/index.html', {'record': record})


def record_detail(request, record_id):
    record = Record.objects.get(id=record_id)
    return render(request, 'record/detail.html', {'record': record})
