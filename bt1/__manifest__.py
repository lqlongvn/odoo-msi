# -*- coding: utf-8 -*-
{
    'name': 'Bài tập 1',
    'version': '1.0',
    'summary': 'Cod Bài tập Order Customer Product',
    'sequence': 1,
    'author': 'Mr. Long, ITPLUS',
    'description': """
        Odoo learn
    """,
    'category': 'Other',
    'website': '',
    'depends': ['sales_team'],
    'data': [
        'wizard/count_order_of_customer_view.xml',
        'views/customer_view.xml',
        'views/order_view.xml',
        'views/order_line_view.xml',
        'views/products_view.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
