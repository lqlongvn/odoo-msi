# -*- coding: utf-8 -*-
{
    'name': 'First Module',
    'version': '1.0',
    'summary': 'Odoo learn',
    'sequence': 1,
    'author': 'ITPLUS',
    'description': """
        Odoo learn
    """,
    'category': 'Other',
    'website': '',
    'depends': ['sales_team'],
    'data': [
        'wizard/employee_leave_reason_view.xml',
        'views/product_view.xml',
        'views/categories_view.xml',
        'views/supplier_view.xml',
        'views/employee_view.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
