from django.db import models

class gig(models.Model):
	"""
	"""
	venueID    = models.ForeignKey('venue')
	date       = models.DateField()
	notes      = models.TextField(blank=True,null=True)
	postID     = models.IntegerField(blank=True, null=True) # This is a function of wordpress
	eventName  = models.CharField(max_length=255,blank=True, null=True)
	tour_id    = models.ForeignKey('tour',blank=True, null=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return '{0} - {1}'.format(self.date,self.venueID.name)

class performance(models.Model):
	"""
	"""
	gigID      = models.ForeignKey('gig')
	time       = models.TimeField()
	link       = models.CharField(max_length=255,blank=True,null=True)
	shortNotes = models.CharField(max_length=255,blank=True,null=True)
	ages       = models.CharField(max_length=255,blank=True,null=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return '{0} - {1} - {2}'.format(self.time,self.gigID.date,self.gigID.venueID.name)

	@models.permalink
	def get_absolute_url(self):
		return ('performance', [int(self.id)])

class tour(models.Model):
	"""
	"""
	name       = models.CharField(max_length=255)
	notes      = models.TextField(blank=True,null=True)
	pos        = models.IntegerField(blank=True,null=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class venue(models.Model):
	"""
	"""
	name       = models.CharField(max_length=255)
	address    = models.TextField(blank=True,null=True)
	city       = models.CharField(max_length=255,blank=True,null=True)
	state      = models.CharField(max_length=255,blank=True,null=True)
	country    = models.CharField(max_length=255,blank=True,null=True)
	postalCode = models.CharField(max_length=255,blank=True,null=True)
	contact    = models.CharField(max_length=255,blank=True,null=True)
	phone      = models.CharField(max_length=255,blank=True,null=True)
	email      = models.CharField(max_length=255,blank=True,null=True)
	link       = models.CharField(max_length=255,blank=True,null=True)
	notes      = models.TextField(blank=True,null=True)
	private    = models.BooleanField()
	apiID      = models.IntegerField(blank=True,null=True)
	deleted    = models.BooleanField()
	customMap  = models.CharField(max_length=255,blank=True,null=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return '{0} - {1} - {2}'.format(self.name,self.city,self.country)

