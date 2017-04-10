# -*- coding: utf-8 -*-

import requests
import csv
from requests.exceptions import HTTPError

from odoo import exceptions
from . import exceptions as BulkSMSExceptions
from user_account import EAPI

VALID_PARAMS_SEND_SMS = ['msisdn', 'dest_group_id', 'sender', 'msg_class',
                         'dca', 'want_report', 'routing_group', 'source_id',
                         'repliable', 'strip_dup_recipients', 'stop_dup_id',
                         'send_time', 'send_time_unixtime',
                         'send_time_seconds', 'scheduling_description',
                         'test_always_succeed', 'test_always_fail',
                         'allow_concat_text_sms', 'concat_text_sms_max_parts',
                         'replace_msg_id', 'protocol_id', ]
# TODO test encoding
def send_sms(username, password, message, quote_sms=False, **kwargs):
    '''
    Sends the SMS
    @param username: bulkSMS EAPI username
    @param password: bulkSMS EAPI password
    @param message: The body of the SMS message.
    @param **kwargs: Valid keys are on the VALID_PARAMS_SEND_SMS
    @return: True on success
    '''
    if not username or not password or not message:
        raise exceptions.MissingError('Provide username password and message.')
    for param in kwargs.keys():
        if param not in VALID_PARAMS_SEND_SMS:
            raise exceptions.UserError(
                msg='''Paramerer {0} is invalid,
                    valid params for sending an SMS are {1}'''
                    .format(param, VALID_PARAMS_SEND_SMS))
    try:
        request = requests.Request('POST', '{EAPI}/submission/{type}/2/2.0'
                                    .format(EAPI=EAPI, type='send_sms' if not quote_sms else 'quote_sms'),
                                    params={'username': username,
                                            'password': password,
                                            'message': message}.update(kwargs))
        response = requests.Session().send(request)
        if response.ok and response.text.split('|')[0] in [0, 1]:
            return True
        else:
            raise BulkSMSExceptions.GenericError(response.text.split('|'))
    except HTTPError as error:
        raise exceptions.Warning(msg='''An error occured while sending SMS.
                        Info: {} \n {}'''.format(error.response.status_code,
                                                 error.response.reason))


VALID_PARAMS_SEND_BATCH = ['batch_data', 'sender', 'msg_class',
                           'dca', 'want_report', 'routing_group', 'source_id',
                           'repliable', 'stop_dup_id',
                           'send_time', 'send_time_unixtime',
                           'send_time_seconds', 'scheduling_description',
                           'test_always_succeed', 'test_always_fail']

VALID_FIELDS_BATCH = ['msisdn', 'message', 'sender', 'msg_class', 'dca',
                      'routing_group', 'source_id', 'repliable']

# TODO Parameter values should be encoded in ISO-8859-1
# batch_data should be CSV (number, message) URL encoded?
def send_batch(username, password, batch_data, **kwargs):
    if not username or not password or not batch_data:
        raise exceptions.MissingError('Provide username password and batch_data')
    _csv = csv.DictReader(batch_data)
    for field in _csv.fieldnames():
        if field not in VALID_PARAMS_SEND_BATCH:
            raise exceptions.MissingError(
                msg='''Paramerer {0} is invalid,
                    valid params for sending an SMS are {1}'''
                    .format(field, VALID_FIELDS_BATCH))
    for param in kwargs.keys():
        if param not in VALID_PARAMS_SEND_BATCH:
            raise exceptions.UserError('''Parameter {0} is invalid
                                        valid params for sending batch SMS are
                                        {1} '''.format(
                                            param, VALID_PARAMS_SEND_BATCH))
    try:
        request = requests.Request('POST', '{EAPI}/submission/send_batch/1/1.0'
                                   .format(EAPI=EAPI), params={'username': username,
                                                               'password': password,
                                                               'batch_data': batch_data}.update(kwargs))
        response = requests.Session().send(request)
        if response.ok and response.text.split('|')[0] in [0, 1]:
            return True
        else:
            raise BulkSMSExceptions.GenericError(response.text.split('|'))
    except HTTPError as error:
        raise exceptions.Warning(
            msg='''An error occured while sending batch SMS.
            Info {} \n {}'''.format(error.response.status_code,
                                    error.response.reason))

    def quote_sms(username, password, message, **kwargs):
        '''
        Returns a quote for the SMS that is to be send.
        @param username: BulkSMS username
        @param password: BulkSMS password
        @param message: Your message
        @param param: **kwargs See method's documentation on BulkSMS.com
        '''
        return send_sms(username, password, message, quote_sms=True, **kwargs)
