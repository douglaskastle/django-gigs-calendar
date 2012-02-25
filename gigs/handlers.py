from piston.handler import BaseHandler
from django.db.models import get_model

class IngestHandler(BaseHandler):
	allowed_methods = ('POST',)

	def __init__(self):
		self.response = {'ok': False}
	
# 	@throttle(60, 60)
	def create(self, request):
		self.response = {'ok': False}
		r = request.POST
		keys = r.keys()
		if 'id' in keys and 'model' in keys:
			try:
				m = get_model('gigs', r['model'])
				try:
					s = m.objects.get(rid=r['id'])
				except:
					s = m()
				
				s.rid = r['id']
				for k in s.__dict__.keys():
					if k in keys and not k == 'id':
						a = r[k]
						if a == 'None':
							a = None
						setattr(s,k,a)
				s.save()
				self.response = {'ok': True, 'id': s.id}
			except:
				pass

		return self.response
