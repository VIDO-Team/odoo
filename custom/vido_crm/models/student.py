# -*- coding: utf-8 -*-

from tkinter import Button
from odoo import models, fields, api, http
import odoo
import json

class vido_crm(models.Model):
    _name = 'student'
    _description = 'thong tin models sinh vien'

    Name = fields.Text(string ='Name', required=True)
    MSSV = fields.Text(string ='MSSV', required=True)
    Ngaysinh = fields.Integer(string='Ngaysinh', default=1)
    Thangsinh = fields.Integer(string='Thangsinh', default=1)
    Namsinh = fields.Text(string='Namsinh', required=True)
    Gender = fields.Selection([
        ('male', 'Male'),
        ('female','Female')
    ], required=True, default = 'male')
    SDT = fields.Text(string = 'SDT', required=True)
    Status = fields.Boolean(string='Status', required=True)
    UpdateDatetime = fields.Date(string='UpdateDatetime', required=False)
    ResponseStatus = fields.Selection([
        ('chưa phản hồi', 'Chưa phản hồi'),
        ('đã phản hồi','Đã phản hồi')
    ], required=True, default = 'chưa phản hồi')


    def action_getApi(self):
        import requests
        
        dataUser = {
            'name': self.Name + self.MSSV,
            'isComplete': self.Status
        }
        headers = {"Content-Type": "application/json", "Accept": "application/json", "Catch-Control": "no-cache"}
        res = requests.post("http://localhost:5108/api/todoitems", data=json.dumps(dataUser), headers=headers)
        print('Resutl content: ',res.content)
        return res.content
    def get_token(self):
        import requests
    
        res = requests.get("http://localhost:5163/api/message/accesstoken")
        print('Resutl content: ',res.content)
        return res.content