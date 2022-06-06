from ensurepip import version
import xmlrpc.client

url = 'http://localhost:8069'
db = 'odooDB'
username = 'admin'
password = 'admin'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
version = common.version()
print('detail')