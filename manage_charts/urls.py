from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^make/', views.make, name='manage_charts_make'),
    url(r'^(?P<song_id>[0-9]+)/$', views.show_chart, name='manage_charts_show'),
    url(r'^$', views.home, name='manage_charts_home'),
]
