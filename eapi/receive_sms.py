# -*- coding: utf-8 -*-
import requests
import csv
import cStringIO
from user_account import EAPI
from exceptions import GenericError

FIELDNAMES = ('msg_id', 'sender', 'message', 'recieved_time', 'msisdn',
              'refering_batch_id', 'encoding')


def get_inbox(username, password, last_retrieved_id):
    request = requests.Request(method='POST',
                               url='{}/reception/get_inbox/1/1.1'.format(EAPI),
                               params={'username': username,
                                       'password': password,
                                       'last_retrieved_id': last_retrieved_id})
    request.prepare()
    response = requests.Session().send(request)
    if response.ok:
        f = cStringIO.StringIO(response.text)
        for line in csv.DictReader(f, fieldnames=FIELDNAMES, delimiter='|'):
            print(line)
            if line.line_num == 1:
                status_code = line[0]
                status_description = line[1]
                extra_info = line[2]
                if status_code != 0:
                    raise GenericError(status_code, status_description, extra_info)
            elif line.line_num == 2:
                continue
            else:
                # TODO save sms on our model
                pass
