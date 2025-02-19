# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# Copyright (c) 2011 CCI Connect asbl (http://www.cciconnect.be) All Rights Reserved.
#                       Philmer <philmer@cciconnect.be>
{
    'name': 'GESTION POINTEUSE',
    'version': '1.0',
    'category': '',
    'description': """
              Gestion de la pointage
    """,
    'depends': ['base',"report_xlsx"],
    'data': [
           'security/ir.model.access.csv',
           "views/centrale.xml",
           "views/pointage.xml",
           "wizard/vider_table_centrale.xml",
           "wizard/wizard_pointeuse.xml",
           "views/menu.xml"
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
