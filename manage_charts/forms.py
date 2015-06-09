from django import forms
import autocomplete_light
from manage_charts.models import ChordChart


class TransposeForm(forms.Form):
    semitones = forms.IntegerField(label='')
    


                                       
