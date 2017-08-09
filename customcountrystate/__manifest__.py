# -*- coding: utf-8 -*-
{
    'name': "country custom fields",

    'summary': """
       Depends VMS vechicle management system country code""",

    'description': """
        Used along with vechicle management system dependent. Study purpose
    """,

    'author': "VA",
    'website': "http://viki2.odoo.com",

    'category': 'Custom',
    'version': '10.0',

    'depends': ['base',
                ],

    'data': [
        'views/countrystate_view.xml',
        'views/base_countrystate_view.xml',
    ],
    'demo': [
        #'demo/demo.xml',
    ],
}
