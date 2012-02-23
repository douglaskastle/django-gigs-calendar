from django.conf.urls.defaults import patterns, include, url
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from gigs.handlers import IngestHandler
from views import *

urlpatterns = patterns('',
    url(r'^all/$', ical, {'full':True}, name='ical-all'),
    url(r'^upcoming/$', ical, name='ical-upcoming'),
    url(r'^performance/(\d+)/$', performance, name='performance'),
#     url(r'^performance/$', performances, name='performances'),
	url(r'^ingest/', Resource(IngestHandler), { 'emitter_format': 'json' }),
)
