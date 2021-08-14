# -*- coding: utf-8 -*-
{
    'name': 'thi_2',
    'version': '1.0',
    'summary': 'Thi 2 project summary',
    'sequence': 1,
    'author': 'Long (Thi 2)',
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
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
