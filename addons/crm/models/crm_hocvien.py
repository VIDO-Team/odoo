from contextlib import nullcontext
from datetime import datetime
from dbm import dumb
from email.policy import default
from pkgutil import simplegeneric
from tkinter import Button
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
    heDaoTaoId = fields.Many2one('crm.hedaotao', string='Hệ đào tạo')
    nganhId = fields.Many2one('crm.nganhhoc', string='Ngành học', )
    chuyenNganhId = fields.Many2one('crm.chuyennganh', string="Chuyên ngành",)
    khoiNganhId = fields.Many2one('crm.khoinganh', string='Khối ngành', )
    

    def action_Chuyennganh(self):
        conn = pymssql.connect(server='DESKTOP-V81VHDR\CDVDL2', user='cdvdl2', password='CDVD@lau2', database='QLDT')
        cursor = conn.cursor()
        conPG = psycopg2.connect(dbname="mydb", user="odoo", password="Vido@01", host="localhost", port="5432")
        print("Database opened successfully")
        cur = conPG.cursor()
        query = 'SELECT * from tbl_QLDT_CTDT_ChuyenNganh'
        cursor.execute(query)
        records = cursor.fetchall()
        print(records)
        for item in records:
            insert_sql = """INSERT INTO crm_chuyennganh ("id", "ma", "ten", "nganhId", "tenTA", "kyHieu")
                            VALUES('{Id}', '{Ma}', '{Ten}', {Nganh}, '{TenTA}','{KyHieu}')""".format(
                                Id = item[0],
                                Ma = item[1].strip(),
                                Ten = item[2],
                                Nganh = json.dumps(item[3]),
                                TenTA = item[4],
                                KyHieu = item[5])
            print(insert_sql)
            cur.execute(insert_sql)
        return conPG.commit()

    def action_Khoinganh(self):
        conn = pymssql.connect(server='DESKTOP-V81VHDR\CDVDL2', user='cdvdl2', password='CDVD@lau2', database='QLDT')
        cursor = conn.cursor()
        conPG = psycopg2.connect(dbname="mydb", user="odoo", password="Vido@01", host="localhost", port="5432")
        print("Database opened successfully")
        cur = conPG.cursor()
        query = 'SELECT * from tbl_QLDT_CTDT_KhoiNganh'
        cursor.execute(query)
        records = cursor.fetchall()
        print(records)
        for item in records:
            insert_sql = """INSERT INTO crm_khoinganh ("id","ma", "ten", "khoaHoc", "soTinChi", "soHocKy")
                            VALUES('{Id}', '{Ma}', '{Ten}', '{KhoaHoc}','{SoTinChi}', '{SoHocKy}')""".format(
                                Id = item[0],
                                Ma = item[1].strip(),
                                Ten = item[2],
                                KhoaHoc = item[3],
                                SoTinChi = item[4],
                                SoHocKy = json.dumps(item[5]))
            print(insert_sql)
            cur.execute(insert_sql)
        return conPG.commit()

    def action_Nganhhoc(self):
        conn = pymssql.connect(server='DESKTOP-V81VHDR\CDVDL2', user='cdvdl2', password='CDVD@lau2', database='QLDT')
        cursor = conn.cursor()
        conPG = psycopg2.connect(dbname="mydb", user="odoo", password="Vido@01", host="localhost", port="5432")
        print("Database opened successfully")
        cur = conPG.cursor()
        query = 'SELECT * from tbl_QLDT_CTDT_Nganh'
        cursor.execute(query)
        records = cursor.fetchall()
        print(records)
        for item in records:
            insert_sql = """INSERT INTO crm_nganhhoc ("id","ma", "ten", "khoiThi", "khoaId", "heDaoTaoId", "tenTA", "kyHieu")
                            VALUES('{Id}', '{Ma}', '{Ten}', '{KhoiThi}',{Khoa}, '{HeDaoTao}', '{TenTA}', '{KyHieu}')""".format(
                                Id = item[0],
                                Ma = item[1].strip(),
                                Ten = item[2].strip(),
                                KhoiThi = item[3].strip(),
                                Khoa = json.dumps(item[4]),
                                HeDaoTao = item[5],
                                TenTA = item[6].strip(),
                                KyHieu = item[7].strip())
            print(insert_sql)
            cur.execute(insert_sql)
        return conPG.commit()


    # def action_UpdateHDT(self):
    #     conn = pymssql.connect(server='DESKTOP-V81VHDR\CDVDL2', user='cdvdl2', password='CDVD@lau2', database='QLDT')
    #     cursor = conn.cursor()
    #     conPG = psycopg2.connect(dbname="mydb", user="odoo", password="Vido@01", host="localhost", port="5432")
    #     print("Database opened successfully")
    #     cur = conPG.cursor()
    #     query = 'SELECT * from tbl_QLDT_CTDT_HeDaoTao'
    #     cursor.execute(query)
    #     records = cursor.fetchall()
    #     print(records)
    #     for item in records:
    #         update_sql = """UPDATE crm_hedaotao ("id","ma", "ten", "tenTA", "hinhThucDaoTaoId", "kyHieu")
    #                         SET ('{Id}', '{Ma}', '{Ten}', '{TenTA}',{HinhThucDaoTao}, '{KyHieu}')""".format(
    #                             Id = item[0],
    #                             Ma = item[1].strip(),
    #                             Ten = item[2].strip(),
    #                             TenTA = item[3].strip(),
    #                             HinhThucDaoTao = json.dumps(item[4]),
    #                             KyHieu = item[5].strip())
    #         print(update_sql)
    #         cur.execute(update_sql)
    #     return conPG.commit()
    

