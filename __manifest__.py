# -*- coding: utf-8 -*-
{
    'name': "Bulksms Integration",

    'summary': """
        Allows you to send sms using Bulksms.com""",

    'description': """
        With bulksms integration module you are now able to send sms messages to your clients. 
        Select a client to send her an SMS message by clicking the `Send SMS` button on the customer form.
        You can also use a new Server Action named `Send SMS` that gives you the opportunity to send SMS.
        A Scheduled Action has also been created and can be customized by you to send SMS when needed.
        Mass SMS sending campaings are also supported.
        On Settings -> Technical -> BulkSMS -> Settings you can set up your credentials
        On Settings -> Technical -> BulkSMS -> Reporting you can see a dynamic report of your SMS.
        Anything that you have sent, received, dates etc.
    """,

    'author': "George Daramouskas",
    'website': "george.daramouskas@gmail.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/res_partner.xml',
    ],
   'application':True
}