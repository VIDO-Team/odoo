# -*- coding: utf-8 -*-
import json
from odoo import http
import odoo
import logging
_logger = logging.getLogger(__name__)

class VidoCrm(http.Controller):
    @http.route(['/api/sinhvien/<dbname>/<id>'], type='http', auth="none", sitemap=False, cors='*', csrf=False)
    def pet_handler(self, dbname, id, **kw):
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


