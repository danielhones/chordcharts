from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^edit/(?P<song_id>[0-9]+)/$', views.edit_chart, name='manage_charts_edit_chart'),
    url(r'^edit/', views.edit_chart, name='manage_charts_edit'),
    url(r'^(?P<song_id>[0-9]+)/$', views.show_chart, name='manage_charts_show'),
    url(r'^$', views.home, name='manage_charts_home'),
]
