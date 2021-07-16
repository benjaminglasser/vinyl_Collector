from django.shortcuts import render, redirect
from .models import Record, Artist
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import ArtistForm


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
    artist_record_doesnt_have = Artist.objects.exclude(
        id__in=record.artists.all().values_list('id'))

    artist_form = ArtistForm()
    return render(request, 'record/detail.html', {
        'record': record,
        'artist_form': artist_form,
        'artist': artist_record_doesnt_have
    })


class RecordCreate(CreateView):
    model = Record
    fields = ['title', 'genre', 'year']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class RecordUpdate(UpdateView):
    model = Record
    fields = ['title', 'genre', 'year']


class RecordDelete(DeleteView):
    model = Record
    success_url = '/records/'

# Artist Views


def add_artist(request, record_id):
    form = ArtistForm(request.POST)
    if form.is_valid():
        new_artist = form.save(commit=False)
        new_artist.record_id = record_id
        new_artist.save()
    return redirect('detail', record_id=record_id)


def assoc_artist(request, record_id, artist_id):
    Record.objects.get(id=record_id).artists.add(artist_id)
    return redirect('detail', record_id=record_id)


class ArtistList(ListView):
    model = Artist


class ArtistDetail(DetailView):
    model = Artist


class ArtistUpdate(UpdateView):
    model = Artist
    fields = ['name', 'members']


class ArtistDelete(DeleteView):
    model = Artist
    success_url = '/artists/'
