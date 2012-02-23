# coding=utf8
from pysqlite2 import dbapi2 as sqlite
# import sqlite3
import re
import csv
import shlex
import time
from datetime import datetime


class sqlobj():
	id = None
	
	def __repr__(self):
		return '{0}'.format(self.id,)

# con = sqlite3.connect(':memory:')
# con = sqlite3.connect('gigs/test.sqlite')

def parse_sql(filename):

	f = open(filename,'r')
	sql = f.read()

	sql = re.sub('--\n','\n',sql)
	sql = re.sub('--.+\n','\n',sql)
	sql = re.sub('\n','',sql)
	sql = re.sub('\\\\n','\n',sql)
	sql_commands = sql.split(';')

	s_list = {}
# 	print sql_commands
	for x in sql_commands:
# 		if x.lower().startswith('create'):
# 			print x
# 			f = re.search('\(.+\)',x)
# 			elements = f.group(0).split(',')
# # 			print elements
# 			for m in elements:
# 				x = re.search('`.+`',m)
# 				attr = re.sub('`','',x.group(0))
# 				if not re.search('PRIMARY KEY',m):
# 					print attr
# # 					setattr(table,attr, None)

		if x.lower().startswith('insert'):
# 			print x
			f = re.search('values',x.lower())
			elements = str(x[f.end()+1:-1]).split('),(')
			e = re.search('`[a-zA-Z0-9_]+`',x[:f.start()])
			table = x[e.start()+1:e.end()-1]
			g = re.search('\(.+\)',x[:f.start()])
			h = x[g.start()+1:g.end()-1]
			h = re.sub('[`\ ]','',h)
			contents = h.split(',')
# 			print contents
			s_list[table] = []
			for m in elements:
				s = sqlobj()
# 				print m
				n = shlex.shlex(m, posix=True)
				n.whitespace += ','
				n.whitespace_split = True
				t = list(n)
# 				print t
				if not len(contents) == len(t):
					print "Warning, len(contents) != len(t)"
					exit()
			
				for i in range(len(t)):
					#print contents[i], t[i]
					if t[i].lower() == 'null' or t[i].lower() == '' :
						setattr(s,contents[i],None)
					else:
						setattr(s,contents[i],t[i])
			
				#print s.__dict__
				s_list[table].append(s)
	return s_list

if __name__ == "__main__":

	s_list = parse_sql('gigs/test.sql')
	print s_list
# 	exit()
	
	con = sqlite.connect('gigs.sqlite')
	cur = con.cursor()
	for s in s_list.keys():
# 		print s, s_list[s]
		g = re.sub('wp_6kf4dh_','',s)
		values = s_list[s][0].__dict__.keys()
		x = ', '.join(values)
# 		try:
# 			cmd = '''drop table {0}'''.format(g,)
# 			print cmd
# 			cur.execute(cmd)
# 		except:
# 			pass
# 		continue
		try:
			cmd = '''create table {0} ({1})'''.format(g,', '.join(values))
			cur.execute(cmd)
		except:
			pass
		
		cmd = '''select * from {0}'''.format(g)
		cur.execute(cmd)
		r = cur.fetchall()
		col_list = [tuple[0] for tuple in cur.description]
		django_values = []
		for v in values:
			for c in col_list:
				if c.startswith(v):
					django_values.append(c)
		if 'created_at' in col_list:
			django_values.append('created_at')
		if 'updated_at' in col_list:
			django_values.append('updated_at')
# 		print django_values
# 		exit()
		for t in s_list[s]:
			w = []
			for v in values:
# 				print v
				x = getattr(t,v)
				try:
					int(x)
					int_true = True
				except:
					int_true = False
				
# 				int_true = False
				if x == None:
					w.append('NULL')
				elif int_true:
					w.append(x)
				elif isinstance(x,str):
					w.append("\""+x+"\"")
				else:
					w.append(x)
			
			if 'created_at' in django_values:
				w.append("\""+str(datetime.now())+"\"")
			if 'updated_at' in django_values:
				w.append("\""+str(datetime.now())+"\"")
# 			print w
# 			exit()
			
			
			cmd = '''select * from {0} where id="{1}"'''.format(g,t.id)
			cur.execute(cmd)
			r = cur.fetchall()
# 			print cmd
# 			print r
			if len(r) == 0:
				cmd = '''insert into {0} ({1}) values ({2})
				'''.format(g,', '.join(django_values),', '.join(w))
				print cmd
				cur.execute(cmd)
		con.commit()
# 			exit()	
	con.commit()
	cur.close()

