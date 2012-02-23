from django.http import HttpResponse
from django.db.models import get_model
import simplejson as json
from icalendar import Calendar, Event, UTC
from datetime import datetime, timedelta
from django.contrib.sites.models import Site
from django.shortcuts import render_to_response
from django.template import RequestContext
import re

p = get_model('gigs', 'performance')

def ical(request, full=False):
	"""
	"""
	cal = Calendar()
	site = Site.objects.get_current()
	
	if full:
		cal_type = 'Full'
	else:
		cal_type = 'Upcoming'
	cal.add('prodid','-//{0} Events Calendar//{1}//EN'.format(cal_type, site.domain))
	cal.add('version','2.0')

	performances = p.objects.all()
	for performance in performances:
		gig = performance.gig
		start = datetime.strptime('{0} {1}'.format(gig.date, performance.time), "%Y-%m-%d %H:%M:%S")
		if start > datetime.now() or full:
			end = start + timedelta(hours=2)
			ical_event = Event()
			ical_event.add('summary','{0}, {1}, {2}'.format(gig.venue.name, gig.venue.city, gig.venue.state))
			ical_event.add('dtstart',start)
			ical_event.add('dtend',end)
			ical_event.add('description','http://{0}{1}'.format(site.domain,performance.get_absolute_url()))
			cal.add_component(ical_event)

	response = HttpResponse(cal.as_string(), mimetype='text/calendar')
	response['Filename'] = 'filename.ics'
	response['Content-Disposition'] = 'attachment; filename=filename.ics'
	return response

def performance(request,id, html_template='gigs/performance.html'):
	"""
	"""
	performance = p.objects.get(id=id)
	gig = performance.gig
	venue = gig.venue
# 	venue.address = re.sub('\n','<br />',venue.address)
	
	context = RequestContext(request, {
		'performance': performance,
		'gig': gig,
		'venue': venue,
	})
	return render_to_response(html_template, context)

	response = {}
	status_code = 200
	body = json.dumps(response, indent=4)
	return HttpResponse(body, status=status_code)
