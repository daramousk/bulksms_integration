# -*- coding: utf-8 -*-

from odoo import exceptions


class GenericError(exceptions.except_orm):
    
    def __init__(self, args):
        super(GenericError, self).__init__('An error occured, here is some info: \n Error code: {error_code} \n Error Message: {error_message}'
                                           .format(error_code=args[0], error_message=args[1]))
