from odoo import models, fields, api, http
import odoo
import json

class Payload(models.Model):
    _name = 'Payload'
    _inherit = 'student'
    _description = 'payload'
    
    phone = fields.Text(string='phone', required=False)
    template_id = fields.Text(string='template_id', required=False)
    template_data = fields.Many2one('XNTS',string='template_data')
    tracking_id = fields.Text(string='tracking_id', required=False)

class XNTS(models.AbstractModel):
    _name = 'XNTS'
    _inherit ='Payload'
    _description = 'object in template_data'
    
    truong_hoc = fields.Text(string='truong_hoc', required=False)
    MaHoSo = fields.Text(string='MaHoSo', required=False)
    customer_name = fields.Text(string='customer_name', required=False)