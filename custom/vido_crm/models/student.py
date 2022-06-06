# -*- coding: utf-8 -*-

from odoo import models, fields, api


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
    Status = fields.Integer(string='Status', required=True)
    UpdateDatetime = fields.Date(string='UpdateDatetime', required=False)
    ResponseStatus = fields.Selection([
        ('chưa phản hồi', 'Chưa phản hồi'),
        ('đã phản hồi','Đã phản hồi')
    ], required=True, default = 'chưa phản hồi')
