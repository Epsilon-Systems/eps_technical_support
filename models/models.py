# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class technical_support(models.Model):
#     _name = 'technical_support.technical_support'
#     _description = 'technical_support.technical_support'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
