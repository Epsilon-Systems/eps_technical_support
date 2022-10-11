# -*- coding: utf-8 -*-

from odoo import models, fields, api


class technicalData(models.Model):
    _name = 'technical.data'
    _description = 'technical_data'

    id = fields.Integer(string='ID')
    date = fields.Date(string='Fecha', help='Fecha')
    business_plan = fields.Char(string='Plan Empresarial')
    description = fields.Char(string='Descripción')

class technicalReplacement(models.Model):
    _name = 'technical.replacement'
    _description = 'tecnical_replacement'

    id = fields.Integer(string='ID')
    name = fields.Char(string='Plan')
    users = fields.Many2one('res.partner', string='Usuario')
    product = fields.Many2one('product.template', string='Producto')
    contact = fields.Many2one('res.partner', string='Contacto')
    phone = fields.Char(related='partner_id.phone', string='Teléfono')
    email = fields.Char(related='partner_id.email', string='Email')
    partner_id = fields.Many2one('res.partner', string='Dirección')
    status = fields.Selection([('draft', 'Borrador'),
                               ('sent', 'Confirmado'),
                               ('deliver', 'Entregado'),
                               ('cashed', 'Cobrado'),],
                              string='Estatus')
