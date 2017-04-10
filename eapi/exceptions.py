# -*- coding: utf-8 -*-

from odoo import exceptions


class GenericError(exceptions.except_orm):

    def __init__(self, error_code, error_message, extra_info=None):
        super(GenericError, self).__init__(
            '''An error occured, here is some info:
            Error code: {error_code} Error Message: {error_message} \n
            {extra_info}'''
            .format(error_code=error_code, error_message=error_message,
                    extra_info=extra_info))
