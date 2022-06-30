from asyncio import QueueEmpty
from contextlib import nullcontext
from datetime import datetime
from email.policy import default
from http import server
from pkgutil import simplegeneric
from tkinter import Button

from numpy import insert
from odoo import models, fields, api, http
from odoo.modules.module import get_module_resource 
import odoo
import sys
import json
import pymssql
import psycopg2

class HocVien(models.Model): 
    _name = "crm.hocvien"
    _description = "model học viên của quản lý sinh viên"

    mshv = fields.Char('Mã số học viên')
    ho = fields.Char('Họ')
    ten = fields.Char('Tên')
    chuyenNganhId = fields.Many2one('crm.chuyennganh', string="Chuyên ngành",)
    khoiNganhId = fields.Many2one('crm.khoinganh', string='Khối ngành', )

    def action_Chuyennganh(self):
        conn = pymssql.connect(server='localhost', user='cdvdlau2', password='CDVD@lau2', database='QLDT')
        cursor = conn.cursor()
        conPG = psycopg2.connect(dbname="odoo14", user="odoo", password="Vido@01", host="localhost", port="5432")
        print("Database opened  successfully")
        cur = conPG.cursor()
        query = 'SELECT * from tbl_QLDT_CTDT_ChuyenNganh'
        cursor.excute(query)
        records = cursor.fetchall()
        for item in records:
            insert_sql = """INSERT INTO crm_chuyenganh (id, "Ma", "Ten", "NganhId", "TenTA", "KyHieu")
                            VALUES('{Id}', '{Ma}', '{Ten}', '{Nganh}', '{TenTA}','{KyHieu}')""".format(
                                Id = item[0],
                                Ma = item[1].strip(),
                                Ten = item[2],
                                TenTA = item[3],
                                Nganh = json.dumps(item[4]),
                                KyHieu = item[5])
            print(insert_sql)
            cur.execute(insert_sql)

        return conPG.commit()

