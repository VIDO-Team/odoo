from contextlib import nullcontext
from datetime import datetime
from email.policy import default
from tkinter import Button
from odoo import models, fields, api, http
import odoo
import json
import pymssql


class vido_crm(models.Model):
    _name = 'crm.nganhhoc'
    _description = 'thong tin cua nganh hoc'
    
    ma = fields.Text(string='Ma', required=True)
    ten = fields.Text(string='Ten', required=True)
    khoiThi = fields.Text(string='khoiThi', required=False)
    khoaId = fields.Integer(string='khoaId', required=False, default="")
    heDaoTaoId = fields.Integer(string='hedaotaoId', required=False)
    tenTA = fields.Text(string='TenTA', required=False)
    kyHieu = fields.Text(string='kyHieu', required=True)

    