# -*- coding: utf-8 -*-
import requests
import cStringIO
import csv
from exceptions import GenericError
from user_account import EAPI

OPTIONAL_FIELDS = ('body', 'completed_time', 'created_time', 'credits',
                   'origin_address', 'source_id')


def get_report(username, password, batch_id, msisdn=None, optional_fields=None):
    fields = optional_fields if optional_fields else OPTIONAL_FIELDS
    request = requests.Request('POST', '{}/status_reports/get_report/2/2.0'.format(EAPI=EAPI),
                               params={'username': username, 'password': password,
                                       'batch_id': batch_id, 'msisdn': msisdn,
                                       'optional_fields': fields})
    response = requests.Session().send(request.prepare())
    if response.ok:
        f = cStringIO.StringIO(response.text)
        for line in csv.DictReader(f, fieldnames=fields, delimiter='|'):
            if line.line_num == 1:
                status_code = line[fields[0]]
                status_description = line[fields[1]]
                if status_code != 0:
                    raise GenericError(status_code, status_description)
            elif line.line_num == 2:
                continue
            else:
                # TODO save report on our model
                pass
