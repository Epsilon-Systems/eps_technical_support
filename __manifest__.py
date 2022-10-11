# -*- coding: utf-8 -*-
{
    'name': "Technical Support",

    'summary': """
        Module in charge of registering tickets for technical support""",

    'description': """
        Module that allows registering claims for services and assigning them to Helpdesk
    """,

    'author': "Anibal Arenas",
    'website': "https://www.epsilonsystemsgroup.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Helpdesk',
    'version': '15.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
