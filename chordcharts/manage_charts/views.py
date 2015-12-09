from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import ChordChart
from chords.chords import Song
from .forms import TransposeForm, ChordChartForm


CHART_EXAMPLE = '|D-7\t|G7\t|Cmaj7\t|.||'


@login_required
def home(request):
    # TODO: Make this an actually usable web page, including search (maybe with autocomplete) and maybe
    # make the complete list of songs its own web page (or pages eventually)
    context = {
        'song_list': list(ChordChart.objects.all()),
        }
    return render(request, 'manage_charts/home.html', context)


# TODO: a class based method for parse_plaintext might look cleaner
@csrf_exempt
def parse_plaintext(request, *args, **kwargs):
    if request.method == 'POST':
        # TODO: Clean this up, SONG_ATTRS doesn't belong here.  It should be in either ChordChart model
        # or the Song class in chords.py:
        # TODO: Should we bother validating the form here?
        SONG_ATTRS = ('title', 'artist', 'album')
        song = {}
        for field in SONG_ATTRS:
            try:
                song[field] = request.POST[field]
            except KeyError:
                pass

        # TODO: Add a ChartParseError or something in the chords module and catch it here so we can respond
        # with an error when needed.
        chordchart = Song(request.POST['plain_text'])
        context = {
            'song': song,
            'chordchart': chordchart
        }
        return render(request, 'manage_charts/chordchart.html', context)
    else:
        return HttpResponse('POST a plaintext chart to this url to be parsed')


# TODO: A class-based view for edit_chart might be cleaner too
@login_required
def edit_chart(request, *args, **kwargs):
    song_page = '/%s/' % str(kwargs['song_id'])

    if request.method == 'POST':
        form = ChordChartForm(request.POST)

        if 'cancel' in request.POST:
            return redirect(song_page)
        elif form.is_valid():
            if 'song_id' in kwargs:
                song = ChordChart.objects.get(pk=kwargs['song_id'])
                song.plain_text = form.cleaned_data['plain_text']
                song.title = form.cleaned_data['title']
                song.artist = form.cleaned_data['artist']
                song.album = form.cleaned_data['album']
            else:
                song = ChordChart(**form.cleaned_data)
            if 'save' in request.POST:
                # Eventually, this will not directly alter the item in the database but rather
                # send a "pull request" that will go for review before being saved in the database
                song.save()
                return redirect('/%s/' % song.pk)
        else:
            # Something unexpected happen, stay on edit page
            return redirect('/edit' + song_page)

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
    return render(request, 'manage_charts/chordchart-page.html', context)
