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
    _name = 'crm.khoinganh'
    _description = 'thong tin khoi nganh'
    
    Ma = fields.Text(string='Ma', required=True)
    Ten = fields.Text(string='Ten', required=True)
    chuyenNganhId = fields.Integer(string='chuyenNganhId', required=True)
    khoaHoc = fields.Integer(string='khoaHoc', required=True)
    soTinChi = fields.Float(string='soTinChi', required=False)
    soHocKy = fields.Integer(string='soHocKy', required=True)
    
    def name_get(self):
        result = []
        for rec in self:
            Ten = rec.Ten
            result.append((rec.id,Ten))
        return result