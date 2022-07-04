from contextlib import nullcontext
from email.policy import default
from unicodedata import name
from odoo import models, fields, api, http



class vido_crm(models.Model):
    _name = 'crm.gioitinh'
    _description = 'thong tin gioi tinh hoc vien'
    
    GioitinhId = fields.Integer(string='GioitinhId', required=True)
    gioiTinh = fields.Text(string='gioiTinh', required=True)
    
    def name_get(self):
        result = []
        for rec in self:
            gioiTinh = rec.gioiTinh
            result.append((rec.id,gioiTinh))
        return result