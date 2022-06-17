# -*- coding: utf-8 -*-

from contextlib import nullcontext
from datetime import datetime
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
    
    def Send_ZNS(self):
        import requests
        from datetime import datetime
        token = requests.get("http://localhost:5163/api/message/accesstoken")
        
        from ast import literal_eval
        import json
        
        jToken = literal_eval(token.content.decode('utf-8'))
        print("token: ",jToken["accessToken"])
        
        # format_data = 'dd/MM/yyyy'
        # datestr = json.dumps(self.UpdateDatetime, indent=4, sort_keys=True, default=str)
        jdate = datetime.strftime(self.UpdateDatetime, "%d/%m/%Y")
        print('date: ',jdate)
        dataUser = {
            'phone': self.SDT,
            'template_id': self.template_id,
            'template_data':{
                    'he_dao_tao':self.truong_hoc,
                    'ngay_dang_ky':jdate,
                    'customer_name':self.customer_name,
                    'ma_so':self.MaHoSo},
            'tracking_id':self.tracking_id
        }
        headers = {"Content-Type": "application/json", "Accept": "application/json", "Catch-Control": "no-cache", "access-token": jToken["accessToken"]}
        res = requests.post("https://business.openapi.zalo.me/message/template", data=json.dumps(dataUser), headers=headers)
        print('Resutl content: ',res.content)
        return res.content
        
        