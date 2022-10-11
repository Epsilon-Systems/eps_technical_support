# -*- coding: utf-8 -*-

from odoo import models, fields, api


class technicalSupport(models.Model):
    _name = 'technical.support'
    _description = 'technical_support'

    name = fields.Char()
    company = fields.Many2one('res.partner', string='Empresa', help='Empresa a la cual pertenece el reclamo')
    plan = fields.Char(string='Plan')
    dn = fields.Char(string='DN')
    claim_user = fields.Char(string='Usuario', help='Usuario que registra el reclamo')
    claim_date = fields.Date(string='Fecha', help='Fecha de reclamo')
    claim_type = fields.Selection([('FS', 'Falla de Servicio'),
                                   ('SG', 'Seguro'),
                                   ('GT', 'Garantías'),],
                                  string='Tipo de reclamo', help="Tipo de reclamo")
    claim_stage = fields.Selection([('draft', 'Borrador'),
                                    ('sent', 'Confirmado'),
                                    ('deliver', 'Entregado'),
                                    ('cashed', 'Cobrado'),],
                                   string='Estado de reclamo', default='draft')
    user_email = fields.Char(string='Email', help='Correo electrónico del usuario que registra el reclamo')
    note = fields.Text(string='Nota', help='Nota o comentario sobre el reclamo')

    #Seguro
    device = fields.Char(string='Dispositivo')
    doc = fields.Char()
    insurance_doc = fields.Binary(string="Doc")
    second_doc = fields.Char()
    second_insurance_doc = fields.Binary(string='Doc 2')
    third_doc = fields.Char()
    third_insurance_doc = fields.Binary(string='Doc 3')
    fourth_doc = fields.Char()
    fourth_insurante_doc = fields.Binary(string='Doc 4')
    insurance_claim_date = fields.Date(string='Fecha Reclamo')
    response_claim = fields.Char(string='Respuesta reclamo')
    payment_status = fields.Char(string='Estatus del pago')

    #Bonificación
    amount = fields.Float(string='Monto')
    description = fields.Text(string='Descripción')

    #Reemplazo


    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
