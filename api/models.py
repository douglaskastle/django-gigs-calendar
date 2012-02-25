from django.db import models

class rid(models.Model):
	"""
	"""
	db       = models.CharField(max_length=255)
	model    = models.CharField(max_length=255)
	mid      = models.CharField(max_length=255,blank=True,null=True)
	rid      = models.IntegerField(blank=True,null=True)

	def __unicode__(self):
		return '{0} - {1} - {2} - {3}'.format(self.db,self.model,self.mid,self.rid)
