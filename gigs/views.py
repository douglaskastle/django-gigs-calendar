from django.http import HttpResponse
from django.db.models import get_model
import simplejson as json
from icalendar import Calendar, Event
from datetime import datetime, timedelta
from django.contrib.sites.models import Site
from django.shortcuts import render_to_response
from django.template import RequestContext
import re

p = get_model('gigs', 'performance')
g = get_model('gigs', 'gig')

def ical(request, type='Full'):
	"""
	"""
	cal = Calendar()
	site = Site.objects.get_current()
	
	if type.lower() == 'full':
		gigs = g.objects.all()
	else:
		gigs = g.objects.filter(date__gte=datetime.now())

	cal.add('prodid','-//{0} Events Calendar//{1}//EN'.format(type, site.domain))
	cal.add('version','2.0')

	for gig in gigs:
		performances = p.objects.filter(gig=gig.id)
		for performance in performances:
			start = datetime.strptime('{0} {1}'.format(gig.date, performance.time), "%Y-%m-%d %H:%M:%S")
			end = start + timedelta(hours=2)
			ical_event = Event()
			ical_event.add('summary','{0}, {1}, {2}'.format(gig.venue.name, gig.venue.city, gig.venue.state))
			ical_event.add('dtstart',start)
			ical_event.add('dtend',end)
			url = 'http://{0}{1}'.format(site.domain,gig.get_absolute_url())
			ical_event.add('description',url)
			cal.add_component(ical_event)

	response = HttpResponse(cal.as_string(), mimetype='text/calendar')
	response['Filename'] = 'filename.ics'
	response['Content-Disposition'] = 'attachment; filename=filename.ics'
	return response

def gig(request,id, html_template='gigs/gig.html'):
	"""
	"""
	gig = g.objects.get(id=id)
	venue = gig.venue
	performances = p.objects.filter(gig=gig.id)
 	#venue.address = re.sub('\n','<br />',venue.address)
	
	context = RequestContext(request, {
		'performances': performances,
		'gig': gig,
		'venue': venue,
	})
	return render_to_response(html_template, context)

	response = {}
	status_code = 200
	body = json.dumps(response, indent=4)
	return HttpResponse(body, status=status_code)

def gigs(request,type='All',html_template='gigs/gigs.html'):
	"""
	"""
	if type.lower() == 'archive':
		gigs = g.objects.filter(date__lte=datetime.now())
	elif  type.lower() == 'upcoming':
		gigs = g.objects.filter(date__gte=datetime.now())
	else:
		gigs = g.objects.all()
	
	context = RequestContext(request, {
		'type': type,
		'gigs': gigs,
	})
	return render_to_response(html_template, context)

	response = {}
	status_code = 200
	body = json.dumps(response, indent=4)
	return HttpResponse(body, status=status_code)
