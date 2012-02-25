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
		if 'id' in keys and 'model' in keys and 'db' in keys:
			# Temporary security fix
			if not r['db'] == 'gigs':
				return self.response
				
			try:
				n = get_model('api', 'rid')
				try:
					p = n.objects.get(rid=r['id'],db=r['id'],model=r['model'])
				except:
					p = n(rid=r['id'],db=r['id'],model=r['model'])

				m = get_model(r['db'], r['model'])
				try:
					s = m.objects.get(id=p.mid)
				except:
					s = m()

				for k in s.__dict__.keys():
					if k == 'id'\
					or k == 'db'\
					or k == 'model'\
					or k.startswith('_')\
					:
						continue
					
					if k in keys:
						a = r[k]
						if a == 'None':
							a = None
						setattr(s,k,a)
				s.save()

				p.mid = s.id
				p.save()
				self.response = {'ok': True, 'id': s.id}
			except:
				pass

		return self.response
