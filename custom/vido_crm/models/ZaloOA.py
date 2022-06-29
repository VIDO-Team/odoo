from odoo import models, fields, api, http
import odoo
import json

class ZaloOA(models.Model):
    _name = 'zalooa'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'tin nhắn zalo oa'
    
    app_id = fields.Text(string='app_id', required=True)
    sender_id = fields.Text('sender_id',required=True)
    recipient_id = fields.Text(string='recipient_id', required=True)
    event_name = fields.Text(string='event_name', required=True)
    msgText = fields.Text(string='msgText', required=True)
    msg_id = fields.Text(string='msg_id', required=True)
    user_id_by_app = fields.Text(string='user_id_by_app', required=True)
    timestamp = fields.Text(string='timestamp', required=True)
    
    