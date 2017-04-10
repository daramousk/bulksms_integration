# -*- coding: utf-8 -*-

from odoo import models, fields


class sms_message_composer(models.Model):
    _name = 'sms.message.composer'

    sender = fields.Char(string='Sender')
    recepient = fields.Char(string='Recepient')
    body = fields.Text(string='Body')  # TODO prohibitions here
    template_id = fields.Many2one(comodel_name='sms.template', string='Template', domain=[('type', '=', 'sms')])
