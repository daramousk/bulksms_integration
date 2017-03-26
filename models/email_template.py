# -*- coding: utf-8 -*-

from odoo import models, fields


class email_template(models.Model):
    _inherit = 'email.template'

    type = fields.Selection(selection=[('email', 'Email'), ('sms', 'SMS')], string='Type')
