# -*- coding: utf-8 -*-

import requests
from requests.exceptions import HTTPError

from odoo import exceptions
from . import exceptions as BulkSMSExceptions


VALID_PARAMS_SEND_SMS = ['msisdn', 'dest_group_id', 'sender', 'msg_class', 'dca',
                         'want_report', 'routing_group', 'source_id', 'repliable',
                         'strip_dup_recipients', 'stop_dup_id', 'send_time', 'send_time_unixtime',
                         'send_time_seconds', 'scheduling_description', 'test_always_succeed',
                         'test_always_fail', 'allow_concat_text_sms', 'concat_text_sms_max_parts',
                         'replace_msg_id', 'protocol_id', ]


def send_sms(username, password, message, **kwargs):
    if not username or not password or not message:
        raise exceptions.MissingError(msg='Provide username, password and message.')
    for param in kwargs.keys():
        if param not in VALID_PARAMS_SEND_SMS:
            raise exceptions.UserError(msg='Paramerer {0} is invalid, valid params for sending an SMS are '.format(param))
    try:
        response = requests.post(url='{EAPI}/submission/send_sms/2/2.0'.format(EAPI='https://bulksms.vsms.net/eapi/'), **kwargs)
        if response.ok and response.text.split('|')[0] in [0, 1]:
            return True
        else:
            raise BulkSMSExceptions.GenericError(response.text.split('|'))
    except HTTPError as error:
        raise exceptions.Warning(msg='An error occured while sending SMS. HTTP Code: \n {}'.format(error.response.status_code))
        