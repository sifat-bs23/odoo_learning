{
    'name': "librarymanagement",

    'summary': """
    Practice of module
    """,

    'description': """
    This module is build for practicing Odoo
    """,

    'author': "Md. Sifat Hassan",
    'website': "https://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [],

    # always loaded
    'data': [
        'views/author-views.xml',
        'views/book-views.xml',
        'views/customer-views.xml',
        'views/rental-views.xml',
        'views/payment-views.xml',
        'views/menu-items.xml',
        'reports/payment_pdf.xml',
        'reports/report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
