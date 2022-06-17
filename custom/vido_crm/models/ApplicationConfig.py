from odoo import models, fields, api, http
import odoo
import json

class applicationconfig(models.Model):
    _name = 'appcof'
    _description = 'Token cua zalo OA'
    
    AppId = fields.Text(string='AppId', required=True)
    SecretKey = fields.Text(string='SecretKey', required=True)
    RefreshToken = fields.Text(string='RefreshToken', required=True)
    AccessToken = fields.Text(string='AccessToken', required=True)
    LastUpdatedDateTime = fields.Date(string='LastUpdatedDateTime', required=False)