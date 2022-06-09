# -*- coding: utf-8 -*-

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
            "name": self.Name + self.MSSV,
            "isComplete": self.Status 
        }
        print('DataUser: ', dataUser)
        res = requests.post("http://localhost:5108/api/todoitems", params=dataUser)
        print('Resutl: ',json.dumps(res))
        return res.content
