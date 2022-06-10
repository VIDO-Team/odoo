# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

import logging
_logger = logging.getLogger(__name__)

class BatchUpdateWizard(models.TransientModel):
    _name = "student.batchupdate.wizard"
    _description = "Batch update for student model"

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
    
    def multi_update(self):
        ids = self.env.context['active_ids'] # selected record ids
        my_students = self.env["student"].browse(ids)
        new_data = {}
        
        if self.Name:
            new_data["Name"] = self.Name
        if self.MSSV:
            new_data["MSSV"] = self.MSSV
        if self.Ngaysinh:
            new_data["Ngaysinh"] = self.Ngaysinh
        if self.Thangsinh:
            new_data["Thangsinh"] = self.Thangsinh
        if self.Namsinh:
            new_data["Namsinh"] = self.Namsinh
        if self.Gender:
            new_data["Gender"] = self.Gender
        if self.SDT:
            new_data["SDT"] = self.SDT
        if self.Status:
            new_data["Status"] = self.Status
        if self.UpdateDatetime:
            new_data["UpdateDatetime"] = self.UpdateDatetime
        if self.ResponseStatus:
            new_data["ResponseStatus"] = self.ResponseStatus    
            
        my_students.write(new_data)