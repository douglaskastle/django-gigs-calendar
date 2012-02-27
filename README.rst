A django implementation of the gigs-calendar plugin for wordpress
=================================================================

History
-------

I have been using wordpress for years, however recently the security model used has left me a little dismayed.  In the subsequent time I have become very familiar with python and django.  I was investigating whether it would be possible to port a blog of mine over to django.  After looking at django-cms and mezzanine the answer was no.  Sadly the plugins of wordpress are very mature and there too many holes.  I, when not coding do standup comedy on the side and found the plugin `Gigs Calendar`_ by `Dan Coulter`_ very useful.  It has a simple entry of gigs that are performed at venues.  I tweaked the php myself a while back to generate an ics feed that could then be loaded into any calendaring tool. While I hoped it would allow all my adoring fans track me to my many gigs, it's really only used by my wife to organise whether we'll be eating in or out for certain days of the week.

.. _Gigs Calendar: http://wordpress.org/extend/plugins/gigs-calendar/
.. _Dan Coulter: http://blogsforbands.com/

As a mini project, I decided if I could do a effective django clone of the Gigs Calendar plugin. This is it.

Dependancies
------------

* django-piston==0.2.3
* icalendar==2.2
* simplejson==2.3.2
