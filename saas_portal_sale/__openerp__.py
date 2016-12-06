# -*- coding: utf-8 -*-
{
    'name': "Saas Portal Sale",
    'author': "IT-Projects LLC, Ildar Nasyrov",
    'license': 'GPL-3',
    'website': "https://twitter.com/nasyrov_ildar",
    'category': 'SaaS',
    'version': '1.0.0',
    'depends': ['sale', 'saas_portal', 'product_price_factor', 'saas_portal_start'],
    'data': [
        'views/product_template.xml',
        'views/product_view.xml',
        'views/saas_portal.xml',
        'views/account_invoice.xml',
        'views/config_wizard.xml',
        'data/mail_template_data.xml',
        'data/ir_config_parameter.xml',
    ],
}
