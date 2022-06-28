
from odoo import api, fields, models

class KhoiNganh(models.Model): 
    _name = "crm.khoinganh"
    _description = "model Khối Ngành của quản lý sinh viên"

    ma = fields.Char('Mã')
    ten = fields.Char('Tên')
    chuyenNganhId = fields.Many2many('Id chuyên ngành')
    khoaHoc = fields.Integer('Khóa học')
    soTinChi = fields.Float('Số tín chỉ')
    soHocKy = fields.Integer('Số học kỳ')