from django import forms
from manage_charts.models import ChordChart 


class TransposeForm(forms.Form):
    semitones = forms.IntegerField(label='')
    

class ChordChartForm(forms.ModelForm):
    class Meta:
        model = ChordChart
        fields = ['title',
                  'artist',
                  'album',
                  'plain_text']
