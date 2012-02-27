====================
django-gigs-calendar
====================
A django implementation of the gigs-calendar plugin for wordpress
-----------------------------------------------------------------

History
=======

I have been using wordpress for years, however recently the security model used has left me a little dismayed.  In the subsequent time I have become very familiar with python and django.  I was investigating whether it would be possible to port a blog of mine over to django.  After looking at django-cms and mezzanine the answer was no.  Sadly the plugins of wordpress are very mature and there too many holes.  I, when not coding, do standup comedy on the side and found the plugin `Gigs Calendar`_ by `Dan Coulter`_ very useful.  It has a simple entry of gigs that are performed at venues.  I tweaked the php myself a while back to generate an ics feed that could then be loaded into any calendaring tool. While I hoped it would allow all my adoring fans track me to my many gigs, it's really only used by my wife to organise whether we'll be eating in or out for certain days of the week.

.. _Gigs Calendar: http://wordpress.org/extend/plugins/gigs-calendar/
.. _Dan Coulter: http://blogsforbands.com/

As a mini project, I decided if I could do a effective django clone of the Gigs Calendar plugin. This is it.

Requirements
============

Please refer to `requirements.txt`_ for an updated list of required packages.

.. _requirements.txt: https://github.com/douglaskastle/django-gigs-calendar/blob/master/requirements.txt

Installation
============
#) Get from git-hub::

	git clone git@github.com:douglaskastle/django-gigs-calendar.git
	
#) Add gigs and api and to INSTALLED_APPS in settings.py::

	INSTALLED_APPS = (
		...
		'gigs',
		'api',
		...
	)

#)  Import gigs and api URL's somewhere in your
    `urls.py`::

	urlpatterns = patterns('',
	    ...
	    (r'^gigs/', include('gigs.urls')),
	    (r'^api/', include('api.urls')),
	    ...
	)
	
#)  Create required data structure::
    
	./manage.py syncdb

Usage
=====
#) Start the development server: ``./manage.py runserver``
#) Navigate to ``/admin/`` you will find that you can add venues, at venues you can have gigs, it that simple
#) Once gigs have been added you can check use these links::

	/gig/<id>/ # HTML page of the gig that is stored at <id>
	/gigs/gigs-upcoming/ # HTML page of gigs after datetime.now()
	/gigs/gigs-archive/ # HTML page of gigs before datetime.now()
	/gigs/gigs-full/ # HTML page of all listed gigs
	/gigs/ical-upcoming/ # ICS feed of gigs after datetime.now()
	/gigs/ical-upcoming/ # ICS feed of all listed gigs
	
TODO
====

License
=======
This application is released 
under the GNU Affero General Public License version 3.
