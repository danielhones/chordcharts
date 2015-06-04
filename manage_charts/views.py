from django.shortcuts import render
from django.http import HttpResponse
from .models import ChordChart
from chords.chords import ChordChartMaker
from django.conf import settings


def home(request):
    context = {
        'song_list': list(ChordChart.objects.all()),
        }
        
    return render(request, 'manage_charts/home.html', context) 

def make(request):
    pass

def show_chart(request, song_id):
    # TODO: fix the redundancy here.  It's not even necessary to use the get_json() method.
    # And fix these stupid confusing names.  There's got to be a better way.
    song = ChordChart.objects.get(pk=song_id)
    raw_chart = ChordChartMaker(song.plain_text)
    context = {
        'song': song,
        'chordchart': raw_chart,
        }
    return render(request, 'manage_charts/chordchart.html', context)
