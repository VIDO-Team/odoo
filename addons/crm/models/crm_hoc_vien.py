from odoo import api, fields, models

class HocVien(models.Model): 
    _name = "crm.hocvien"
    _description = "model học viên của quản lý sinh viên"

    mshv = fields.Char('Mã số học viên')
    ho = fields.Char('Họ')
    ten = fields.Char('Tên')
    chuyenNganhId = fields.Many2many('crm.chuyennganh', string='Chuyên ngành')
    khoiNganhId = fields.Many2many('crm.khoinganh', string='Khối ngành')

