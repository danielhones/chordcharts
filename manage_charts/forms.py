from django import forms
from manage_charts.models import ChordChart


class TransposeForm(forms.Form):
    semitones = forms.IntegerField(label='')
    


                                       
