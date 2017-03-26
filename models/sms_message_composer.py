# -*- coding: utf-8 -*-

from odoo import models, fields


class sms_message_composer(models.Model):
    _name = 'sms.message.composer'

    sender = fields.Char(string='Sender')
    recepient = fields.Char(string='Recepient')
    body = fields.Text(string='Body')  # TODO prohibitions here
    template_id = fields.Many2one(comodel_name='sms.template', string='Template', domain=[('type', '=', 'sms')])








# import requests
# #from odoo import models, fields, api
# 
# returns = requests.post(url='https://bulksms.vsms.net/eapi/submission/send_sms/2/2.0', data={'username':'gorkygd67', 
#                                                                                    'password':'19001900', 
#                                                                                    'message':u'hello world ō ΓΙΩΡΓΟΣ'.encode('utf_16'),
#                                                                                    'msisdn':'306945049510'})
