# -*- coding: utf-8 -*-
{
    'name': 'thi_1',
    'version': '1.0',
    'summary': 'Thi project summary',
    'sequence': 1,
    'author': 'Long (Thi)',
    'description': """
        Thi project description
    """,
    'category': 'Other',
    'website': '',
    'depends': ['sales_team'],
    'data': [
        'wizard/customer_total_money_view.xml',
        'views/customer_view.xml',
        'views/order_view.xml',
        'views/order_line_view.xml',
        'views/product_view.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
