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

class MyPetAPI(odoo.http.Controller):
    ... # code nhu tren

    @odoo.http.route(['/api/hedaotao'], type='http', auth="none", sitemap=False, cors='*', csrf=False)
    def pet_handler(self, dbname, **kw):
        model_name = "crm.hedaotao"
        try:
            conn = pymssql.connect(server='localhost', user='sincollmm', password='zxcZXCV123', database='QLDT')
            cursor = conn.cursor()  
            query = 'SELECT * from tbl_QLDT_CTDT_HeDaoTao'
            cursor.execute(query)
            records = cursor.fetchall()
            registry = odoo.modules.registry.Registry(dbname)
            with odoo.api.Environment.manage(), registry.cursor() as cr:
                env = odoo.api.Environment(cr, odoo.SUPERUSER_ID, {})
                rec = env[model_name].search([(records)])
                
        except Exception:
            records = {
                "status": "error",
                "content": "not found"
            }
        print(json.dumps(records))
        return json.dumps(records)