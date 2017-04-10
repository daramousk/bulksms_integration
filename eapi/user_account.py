# -*- coding: utf-8 -*-
import requests
import csv
import cStringIO
from exceptions import GenericError

EAPI = 'https://bulksms.vsms.net/eapi/'


def get_credits(username, password):
    request = requests.Request('POST', '{EAPI}/user/get_credits/1/1.1'
                               .format(EAPI=EAPI),
                               params={'username': username, 'password': password})
    response = requests.Session().send(request.prepare())
    if response.ok:
        f = cStringIO.StringIO(response.text)
        for line in csv.reader(f, delimiter='|'):
            status_code = line[0]
            status_description = line[1]
            if status_code != 0:
                raise GenericError(status_code, status_description)
            else:
                # TODO save credits that exist in status_description
                return True

# TODO ISO-8859-1 on param values
def transfer_credits(username, password, to_username, to_userid, _credits, from_comment=None, to_comment=None):
    request = requests.Request('POST', '{EAPI}/user/transfer_credits/1/1.0'
                               .format(EAPI=EAPI),
                               params={'username': username,
                                       'password': password,
                                       'to_username': to_username,
                                       'to_userid': to_userid,
                                       'credits': _credits,
                                       'from_comment': from_comment,
                                       'to_comment': to_comment})
    response = requests.Session().send(request.prepare())
    if response.ok:
        f = cStringIO.StringIO(response.text)
        for line in csv.reader(f, delimiter='|'):
            status_code = line[0]
            status_description = line[1]
            if status_code != 0:
                raise GenericError(status_code, status_description)
            else:
                # TODO save credits that exist in status_description
                return True
