from django.db import models
from chords.chords import ChordChartMaker

# Create your models here.
class ChordChart(models.Model):
    title = models.CharField(max_length=255, default='')
    artist = models.CharField(max_length=255, default='')
    album = models.CharField(max_length=255, default='')
    plain_text = models.TextField(default='')

    def __unicode__(self):
        return '%s - %s from %s' % (self.title, self.artist, self.album)
