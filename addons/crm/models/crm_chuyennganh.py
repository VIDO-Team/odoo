
from odoo import api, fields, models

class ChuyenNganh(models.Model):
    _name = "crm.chuyennganh"
    _description = "model Chuyên Ngành của quản lý sinh viên"

    ma = fields.Char('Mã')
    ten = fields.Char('Tên')
    nganhId = fields.Many2one('Id ngành')
    tenTA = fields.Char('Tên tiếng anh')
    kyHieu = fields.Char('Ký hiệu')
