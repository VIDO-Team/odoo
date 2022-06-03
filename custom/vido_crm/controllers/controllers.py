# -*- coding: utf-8 -*-
# from odoo import http


# class VidoCrm(http.Controller):
#     @http.route('/vido_crm/vido_crm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vido_crm/vido_crm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vido_crm.listing', {
#             'root': '/vido_crm/vido_crm',
#             'objects': http.request.env['vido_crm.vido_crm'].search([]),
#         })

#     @http.route('/vido_crm/vido_crm/objects/<model("vido_crm.vido_crm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vido_crm.object', {
#             'object': obj
#         })
