# -*- coding: utf-8 -*-

from odoo import models, fields, api


class sms_settings(models.TransientModel):
    _inherit = 'res.config.settings'
    _name = 'sms.settings'
    
    username = fields.Char()
    password = fields.Char()

    @api.one
    def set_default_credentials(self):
        settings_holder = self.env['sms.settings.holder']
        rec = settings_holder.search([])[-1]
        if not rec:
            rec = settings_holder.create({})
        rec.write({'username': self.username, 'password': self.password})
        return {'username': self.username, 'password': self.password}

    @api.model
    def get_default_credentials(self, fields):
        settings_holder = self.env['sms.settings.holder']
        rec = settings_holder.search([])[-1]
        if rec:
            return {'username': rec.username, 'password': rec.password}
        else:
            return {}


class sms_settings_holder(models.Model):
    _name = 'sms.settings.holder'
    
    username = fields.Char()
    password = fields.Char()
