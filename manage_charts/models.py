from django.db import models


class ChordChart(models.Model):
    title = models.CharField(max_length=255, default='')
    artist = models.CharField(max_length=255, default='', blank=True)
    album = models.CharField(max_length=255, default='', blank=True)
    plain_text = models.TextField(default='')

    def __unicode__(self):
        return '%s - %s from %s' % (self.title, self.artist, self.album)
