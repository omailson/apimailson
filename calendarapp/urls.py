from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('calendarapp.views',
    url(r'^(?P<name>(\w+))(?P<year>([0-9]{4}))(?P<month>([0-9]{2})).svg$', 'render', name='render'),
    url(r'^(?P<name>(\w+))(?P<year>([0-9]{4}))(?P<month>([0-9]{2})).pdf$', 'renderpdf', name='renderpdf'),
)
