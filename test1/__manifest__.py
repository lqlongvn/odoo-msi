# -*- coding: utf-8 -*-
{
    'name': 'Test-1, first_module',
    'version': '1.0',
    'summary': 'Odoo learn',
    'sequence': 1,
    'author': 'Mr. Long',
    'description': """
        Odoo learn
    """,
    'category': 'Other',
    'website': '',
    'depends': ['sales_team',
                'base'
    ],
    'data': [
        'views/employees_view.xml',
        'views/my_user_view.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
