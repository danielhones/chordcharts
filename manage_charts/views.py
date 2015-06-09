from django.shortcuts import render
from django.http import HttpResponse
from .models import ChordChart
from chords.chords import ChordChartMaker
from django.conf import settings
from .forms import TransposeForm


def home(request):
    context = {
        'song_list': list(ChordChart.objects.all()),
        }
    return render(request, 'manage_charts/home.html', context) 

def make(request):
    pass

def show_chart(request, song_id):
    # TODO: fix the redundancy here. There's got to be a better way.
    song = ChordChart.objects.get(pk=song_id)
    raw_chart = ChordChartMaker(song.plain_text)
    context = {
        'song': song,
        'chordchart': raw_chart,
        'form': TransposeForm(),
        }
    if request.method == 'POST':
        form = TransposeForm(request.POST)
        if form.is_valid():
            semitones = form.cleaned_data['semitones']
            new_form = TransposeForm(initial={'semitones': semitones})
            context['chordchart'] = raw_chart.transpose(semitones)
            context['form'] = new_form
            return render(request, 'manage_charts/chordchart.html', context)
    return render(request, 'manage_charts/chordchart.html', context)

