# -*- coding: utf-8 -*-
{
    'name': 'to_do_list_1',
    'version': '1.0',
    'summary': 'to_do_list project summary',
    'sequence': 1,
    'author': 'Long (to_do_list)',
    'description': """
        to_do_list project description
    """,
    'category': 'Other',
    'website': '',
    'depends': ['sales_team'],
    'data': [
        'views/todolist_view.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
