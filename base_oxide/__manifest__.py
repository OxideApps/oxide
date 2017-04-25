# -*- coding: utf-8 -*-
{
    'name': "Oxide",
    'summary': "Community Powered Odoo Distribution",
    'description': """
        Community Powered Odoo Distribution
    """,
    'author': "Daniel Reis",
    'website': "http://oxideapps.com",
    'version': "10.0.0.1.0",
    'depends': [
        'base',
        'disable_odoo_online',  # OCA/server-tools
        'web_responsive',  # OCA/web
        ],
    'data': [
        'views/assets.xml'
        ],
}
