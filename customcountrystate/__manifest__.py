# -*- coding: utf-8 -*-
{
    'name': "country customfiles",

    'summary': """
       contains 2016 Custom files""",

    'description': """
        Long description of module's purpose
    """,

    'author': "viki",
    'website': "http://viki2.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/countrystate_view.xml',
        'views/base_countrystate_view.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
