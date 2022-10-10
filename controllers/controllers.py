# -*- coding: utf-8 -*-
# from odoo import http


# class TechnicalSupport(http.Controller):
#     @http.route('/technical_support/technical_support', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/technical_support/technical_support/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('technical_support.listing', {
#             'root': '/technical_support/technical_support',
#             'objects': http.request.env['technical_support.technical_support'].search([]),
#         })

#     @http.route('/technical_support/technical_support/objects/<model("technical_support.technical_support"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('technical_support.object', {
#             'object': obj
#         })
