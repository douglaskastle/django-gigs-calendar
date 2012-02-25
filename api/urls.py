from django.conf.urls.defaults import patterns, url
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from api.handlers import IngestHandler

urlpatterns = patterns('',
	url(r'^upload/', Resource(IngestHandler), { 'emitter_format': 'json' }),
)
