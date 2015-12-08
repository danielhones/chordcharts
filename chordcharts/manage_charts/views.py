from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import ChordChart
from chords.chords import Song
from django.conf import settings
from .forms import TransposeForm, ChordChartForm
from collections import namedtuple


# TODO: make edit and chordchart templates load/inherit the same template file to display chord chart
# TODO: also consider making the edit form from its separate elements rather than build from a model,
#       so that you can give textarea autofocus.  (Useful for example when auto updating the preview)


CHART_EXAMPLE = '|D-7\t|G7\t|Cmaj7\t|.||'


@login_required
def home(request):
    context = {
        'song_list': list(ChordChart.objects.all()),
        }
    return render(request, 'manage_charts/home.html', context)



def edit_chart(request, *args, **kwargs):
    if request.method == 'POST':
        # TODO: It doesn't seem like there's much point in making the form a ChordChartForm, then
        # checking if the form is valid.  There's nothing really to validate anyway. response.POST is
        # a query dict that contains all the objects we need, it's the same as form.cleaned_data I think.
        # Consider using form = request.POST instead.
        form = ChordChartForm(request.POST)
        return_to_page = '/'

        if form.is_valid():
            if 'song_id' in kwargs:
                song = ChordChart.objects.get(pk=kwargs['song_id'])
                song.plain_text = form.cleaned_data['plain_text']
                song.title = form.cleaned_data['title']
                song.artist = form.cleaned_data['artist']
                song.album = form.cleaned_data['album']
                return_to_page = '/' + str(song.pk)
            else:
                song = ChordChart(**form.cleaned_data)
            if 'submit' in request.POST:
                # Eventually, this will not directly alter the item in the database but rather
                # send a "pull request" that will go for review before being saved in the database
                song.save()
                return redirect('/%s/' % song.pk)
        if 'preview' in request.POST:
            context = {
                'form': ChordChartForm(instance=song),
                'song': song,
                'chordchart': Song(song.plain_text),
            }
            return render(request, 'manage_charts/edit.html', context)
        elif 'cancel' in request.POST:
            return redirect(return_to_page)

    if 'song_id' in kwargs:
        song = ChordChart.objects.get(pk=kwargs['song_id'])
    else:
        song = ChordChart(title='Example', artist='', album='', plain_text=CHART_EXAMPLE)
    context = {
        'form': ChordChartForm(instance=song),
        'song': song,
        'chordchart': Song(song.plain_text),
    }
    return render(request, 'manage_charts/edit.html', context)


@login_required
def show_chart(request, song_id):
    # TODO: fix the redundancy here. There's got to be a better way.
    song = ChordChart.objects.get(pk=song_id)
    raw_chart = Song(song.plain_text)
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
