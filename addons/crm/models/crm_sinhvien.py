# -*- coding: utf-8 -*-

from contextlib import nullcontext
from datetime import datetime
from email.policy import default
from pkgutil import simplegeneric
from tkinter import Button
from odoo import models, fields, api, http
from odoo.modules.module import get_module_resource 
import odoo
import sys
import json
import pymssql
import psycopg2

class vido_crm(models.Model):
    _name = 'crm.sinhvien'
    _description = 'thong tin models sinh vien'

    Ho = fields.Text(string ='Ho', required=True)
    Ten = fields.Text(string='Ten', required=True)
    MSSV = fields.Text(string ='MSSV', required=True)
    Hinhanh = fields.Text(string='Hinhanh', required=False)
    MaLop = fields.Text(string='MaLop', required=True)
    hedaotaoId = fields.Many2one('crm.hedaotao',string='hedaotaoId')
    nganhId = fields.Many2one('crm.nganhhoc',string='nganhId')
    
    NamNhapHoc = fields.Integer(string='NamNhapHoc', default=1)
    KhoaHoc = fields.Integer(string='KhoaHoc', default=1)
    HoSoId = fields.Integer(string='HoSoId', required=False)
    GhiChu = fields.Text(string='GhiChu', required=False)
    NgayLap = fields.Date(string='NgayLap', required=False)
    MaTrangThai = fields.Text(string='MaTrangThai', required=False)
    Ngaysinh = fields.Date(string='Ngaysinh', required=True)
    Email = fields.Text(string='Email', required=False)
    SDT = fields.Text(string='SDT', required=False)
    CMND = fields.Text(string='CMND', required=False)
    GioiTinh = fields.Selection([
        ('nam', 'Nam'),
        ('nữ','Nữ')
    ], required=False, default = 'nam')
    NguoiLap = fields.Text(string='NguoiLap', required=False)
    NoiSinh = fields.Text(string='Noisinh', required=False)
    
    def action_Hedaotao(self):
        conn = pymssql.connect(server='localhost', user='sincollmm', password='zxcZXCV123', database='QLDT')
        cursor = conn.cursor() 
        conPG = psycopg2.connect(dbname="crmVido", user="odoo", password="vido@01", host="localhost", port="5432") 
        print("Database opened successfully")
        cur = conPG.cursor();
        query = 'SELECT * from tbl_QLDT_CTDT_HeDaoTao'
        cursor.execute(query)
        records = cursor.fetchall()
        for item in records:
            item[1].strip()
            insert_sql = """INSERT INTO crm_hedaotao (Id, Ma, Ten, TenTA, HinhthucdaotaoId, kyHieu) 
                            VALUES('{Id}','{Ma}','{Ten}','{TenTA}','{HinhThuc}','{KyHieu}')""".format(
                                Id = item[0],
                                Ma = item[1].strip(),
                                Ten = item[2],
                                TenTA = item[3],
                                HinhThuc = item[4],
                                KyHieu = item[5])
            print(insert_sql)
            cur.execute(insert_sql)
            
        return conPG.commit()

    # def action_getApi(self):
    #     import requests
        
    #     dataUser = {
    #         'name': self.Name + self.MSSV,
    #         'isComplete': self.Status
    #     }
    #     headers = {"Content-Type": "application/json", "Accept": "application/json", "Catch-Control": "no-cache"}
    #     res = requests.post("http://localhost:5108/api/todoitems", data=json.dumps(dataUser), headers=headers)
    #     print('Resutl content: ',res.content)
    #     return res.content
    
    # def Send_ZNS(self):
    #     import requests
    #     from datetime import datetime
    #     token = requests.get("http://localhost:5163/api/message/accesstoken")
        
    #     from ast import literal_eval
    #     import json
        
    #     jToken = literal_eval(token.content.decode('utf-8'))
    #     print("token: ",jToken["accessToken"])
        
    #     # format_data = 'dd/MM/yyyy'
    #     # datestr = json.dumps(self.UpdateDatetime, indent=4, sort_keys=True, default=str)
    #     jdate = datetime.strftime(self.UpdateDatetime, "%d/%m/%Y")
    #     print('date: ',jdate)
    #     dataUser = {
    #         'phone': self.SDT,
    #         'template_id': self.template_id,
    #         'template_data':{
    #                 'he_dao_tao':self.truong_hoc,
    #                 'ngay_dang_ky':jdate,
    #                 'customer_name':self.customer_name,
    #                 'ma_so':self.MaHoSo},
    #         'tracking_id':self.tracking_id
    #     }
    #     headers = {"Content-Type": "application/json", "Accept": "application/json", "Catch-Control": "no-cache", "access-token": jToken["accessToken"]}
    #     res = requests.post("https://business.openapi.zalo.me/message/template", data=json.dumps(dataUser), headers=headers)
    #     print('Resutl content: ',res.content)
    #     return res.content