from odoo import models, fields, api, http
import odoo
import json

class Payload(models.AbstractModel):
    _inherit ='student'
    _description = 'payload'
    
    template_id = fields.Text(string='template_id', required=False)
    template_data = fields.Many2one('student',string='template_data')
    tracking_id = fields.Text(string='tracking_id', required=False)

class XNTS(models.AbstractModel):
    _inherit ='student'
    _description = 'object in template_data'
    
    truong_hoc = fields.Text(string='truong_hoc', required=False)
    MaHoSo = fields.Text(string='MaHoSo', required=False)
    customer_name = fields.Text(string='customer_name', required=False)