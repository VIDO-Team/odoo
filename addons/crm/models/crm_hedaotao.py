from contextlib import nullcontext
from datetime import datetime
from email.policy import default
from tkinter import Button
from unicodedata import name
from odoo import models, fields, api, http
import odoo
import json
import pymssql


class vido_crm(models.Model):
    _name = 'crm.hedaotao'
    _description = 'thong tin he dao tao'
    
    Ma = fields.Text(string='Ma', required=True)
    Ten = fields.Text(string='Ten', required=True)
    TenTA = fields.Text(string='TenTA', required=False)
    HinhthucdaotaoId = fields.Integer(string='HinhthucdaotaoId', required=False)
    kyHieu = fields.Text(string='kyHieu', required=False)
    
    def name_get(self):
        result = []
        for rec in self:
            Ten = rec.Ten
            result.append((rec.id,Ten))
        return result