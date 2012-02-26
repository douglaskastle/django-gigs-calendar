from django.conf.urls.defaults import patterns, include, url
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from views import *

urlpatterns = patterns('',
    url(r'^ical-upcoming/$', ical, {'type':'Upcoming'}, name='ical-upcoming'),
    url(r'^ical-full/$', ical, {'type':'Full'}, name='ical-full'),
    url(r'^gig/(\w+)/$', gig, name='gig'),
    url(r'^gigs-archive/$', gigs, {'type':'Archive'}, name='gigs-archive'),
    url(r'^gigs-upcoming/$', gigs, {'type':'Upcoming'}, name='gigs-upcoming'),
    url(r'^gigs-full/$', gigs, name='gigs-full'),
)
