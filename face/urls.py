from django.conf.urls import patterns, url


urlpatterns = patterns('face.views',
    url(r'^$', 'index', name='index'),
)
