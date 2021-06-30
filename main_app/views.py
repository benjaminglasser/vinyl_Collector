from django.shortcuts import render


class Vinyl:
    def __init__(self, artist, title, year_of_release, genre):
        self.artist = artist
        self.title = title
        self.year_of_release = year_of_release
        self.genre = genre


vinyl = [
    Vinyl('The Rolling Stones', 'Some Girls', 1978, 'Rock'),
    Vinyl('Nas', 'Illmatic', 1994, 'Hip-Hop'),
    Vinyl('The Flaming Lips', 'The Soft Bulletin', 1999, 'Alternative/Indie'),
    Vinyl('Floating Points', 'Crush', 2019, 'Electronic'),
]


# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def vinyl_index(request):
    return render(request, 'vinyl/index.html', {'vinyl': vinyl})
