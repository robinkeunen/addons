# -*- coding: utf-8 -*-
##############################################################################
#
#    POS Payment Terminal module for Odoo
#    Copyright (C) 2014 Aurélien DUMAINE
#    Copyright (C) 2015 Akretion (www.akretion.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'POS Automatic Cashdrawer',
    'version': '9.0.0.1.0',
    'category': 'Point Of Sale',
    'summary': 'Manage Automatic Cashdrawer device from POS front end',
    'author': "Aurélien DUMAINE",
    'license': 'AGPL-3',
    'depends': ['point_of_sale'],
    'data': [
        'security/res_groups.xml',
        'pos_automatic_cashdrawer_view.xml',
        'account_journal_view.xml',
        'static/src/xml/templates.xml',
        ],
    'qweb': ['static/src/xml/pos_automatic_cashdrawer.xml'],
    'demo': ['pos_automatic_cashdrawer_demo.xml'],
    'installable': True,
}
