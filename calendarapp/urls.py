from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('calendarapp.views',
    url(r'^$', 'home'),
)
