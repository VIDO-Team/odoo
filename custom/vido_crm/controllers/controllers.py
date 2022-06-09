# -*- coding: utf-8 -*-
import json
from pydoc import classname
from sqlite3 import connect
from tokenize import Name
from urllib import response
from odoo import api, http
import odoo
import pymssql
import requests
import logging

_logger = logging.getLogger(__name__)

class GetStudent(http.Controller):
    @http.route(['/api/sinhvien/<dbname>/<id>'], type='http', auth="none", sitemap=False, cors='*', csrf=False)
    def GetStudent(self, dbname, id, **kw):
        model_name = "student"
        try:
            registry = odoo.modules.registry.Registry(dbname)
            with odoo.api.Environment.manage(), registry.cursor() as cr:
                env = odoo.api.Environment(cr, odoo.SUPERUSER_ID, {})
                rec = env[model_name].search([('id', '=', int(id))], limit=1)
                response = {
                    "status": "ok",
                    "content": {
                        "Name": rec.Name,
                        "MSSV": rec.MSSV,
                        "Ngaysinh": rec.Ngaysinh,
                        "Thangsinh": rec.Thangsinh,
                        "Namsinh": rec.Namsinh,
                        "Gender": rec.Gender,
                        "SDT": rec.SDT,
                        "Status": rec.Status,
                        "UpdateDatetime": rec.UpdateDatetime.strftime('%d/%m/%Y'),
                        "ResponseStatus": rec.ResponseStatus,
                    }
                }
        except Exception:
            response = {
                "status": "error",
                "content": "not found"
            }
        return json.dumps(response)

class ConnectMSSQL(http.Controller): 
    # @http.route(['/api/sinhvien'], type='http', auth="none", sitemap=False, cors='*', csrf=False)
    # def connect(self):
    #     conn = pymssql.connect(server='zalovido.pmsa.com.vn', user='vido01', password='Vido@01', database='Vido',port=4020)
    #     cursor = conn.cursor()  
    #     query = 'SELECT * from TodoItems'
    #     cursor.execute(query)
    #     records = cursor.fetchall()
    #     return json.dumps(records)
    
    @http.route(['/api/todoitems'], type='http', auth="none", sitemap=False, cors='*', csrf=False)
    def GetApi(self):
        res = requests.get("http://localhost:5108/api/todoitems")
        return res.content
    
    # @http.route(['/api/todoitems'], type='http', auth="none", sitemap=False, cors='*', csrf=False)
    # def action_getApi(self):
    #     import requests
    #     MealType = http.request.env['student']
    #     mealtypes = MealType.search(['name','=',MealType.get(self.name)])
    #     dataUser = {
    #         'name': self.Name + self.MSSV,
    #         'isComplete': self.Status
    #     }
    #     print(dataUser)
    #     hdr = {
    #         'Content-Type': 'application/json',
    #         'Accept':'application/json'}
    #     res = requests.post("http://localhost:5108/api/todoitems", data=dataUser, headers=hdr)
    #     print('Resutl content: ',res.content)
    #     return res.content
        

# class PostStudent(http.Controller):
#     @http.route(['/api/sinhvien/<dbname>'], type='json', auth="public",sitemap=False, cors='*', csrf=False,methods=['POST'])
#     def PostStudent(self, dbname, **kw):
#         model_name = "student"
#         try:
#             registry = odoo.modules.registry.Registry(dbname)
#             with odoo.api.Environment.manage(), registry.cursor() as cr:
#                 env = odoo.api.Environment(cr, odoo.SUPERUSER_ID, {})
#                 rec = env[model_name].search([('id', '=', int(id))], limit=1)
#                 response = {
#                    "jsonrpc": "2.0",
#                     "id": 'null',
#                     "result": {
#                         "Name": rec.Name,
#                         "MSSV": rec.MSSV,
#                         "Ngaysinh": rec.Ngaysinh,
#                         "Thangsinh": rec.Thangsinh,
#                         "Namsinh": rec.Namsinh,
#                         "Gender": rec.Gender,
#                         "SDT": rec.SDT,
#                         "Status": rec.Status,
#                         "UpdateDatetime": rec.UpdateDatetime.strftime('%d/%m/%Y'),
#                         "ResponseStatus": rec.ResponseStatus,
#                     }
#                 }
#         except Exception:
#             response = {
#                 "status": "error",
#                 "content": "not found"
#             }
#         return json.dumps(response)

