# -*- coding: utf-8 -*-
import unittest
from ..bulksms.receive_sms import get_inbox


class test_receive_sms(unittest.TestCase):

    def test_wrong_username(self):
        get_inbox('gorkygd67', '19001900', 0)
        # TODO self.assertRaises(excClass, callableObj)

    def test_wrong_password(self):
        get_inbox('gorkygd67', '19001901', 0)

    def test_wrong_last_retrieved_id(self):
        get_inbox('gorkygd67', '19001900', 1231)

if __name__ == '__main__':
    unittest.main()
