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
					p = n()
					p.rid = r['id']
					p.db = r['db']
					p.model = r['model']

				m = get_model(r['db'], r['model'])
				try:
					s = m.objects.get(id=p.mid)
# 					s = m.objects.get(rid=r['id'])
				except:
					s = m()
				p.mid = s.id
				p.save()
				

# 				s.rid = r['id']
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
				self.response = {'ok': True, 'id': s.id}
			except:
				pass

		return self.response
