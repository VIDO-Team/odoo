import xmlrpc.client

url = 'http://localhost:8069'
db = 'OdooVidoDB'
username = 'admin'
password = 'admin'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
common.version()
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
#read
resutl = models.execute_kw(db, uid, password, 'res.partner', 'search_read', [[['is_company', '=', True]]], {'fields': ['name', 'country_id', 'comment'], 'limit': 5})
print('resutl: ', resutl)
#create
id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{'name': "sincollmm"}])
print('resutl create id: ',id)