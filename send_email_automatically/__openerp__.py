# -*- coding: utf-8 -*-
{
    'name': "send_email_automatically",

    'summary': """
    Send email using a module
        """,

    'description': """
        Based on https://travs-w.github.io/2015/05/05/send-email-odoo-partner.html
    """,

    'author': "Your Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'analytic'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/button_send_contract.xml',
        'templates.xml',


    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}