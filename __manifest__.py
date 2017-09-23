# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright ODOOBRO.CONTACT@GMAIL.COM
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
    'name': 'OdooBro Website',
    'version': '1.0',
    'category': 'Theme/OdooBro',
    'author': 'OdooBro',
    'website': '',
    'license': 'AGPL-3',
    'depends': [
        'website_blog', 'website_form'
    ],
    'data': [
        # ============================================================
        # SECURITY SETTING - GROUP - PROFILE
        # ============================================================
        # 'security/',
        # 'security/ir.model.access.csv',

        # ============================================================
        # DATA
        # ============================================================
        # 'data/',

        # ============================================================
        # VIEWS
        # ============================================================
        'views/frontend/odoobro_menu.xml',
        'views/frontend/odoobro_layout.xml',
        'views/frontend/odoobro_templates.xml',
        'views/frontend/odoobro_homepage.xml',

        'views/backend/ob_customer_question_view.xml',
        # ============================================================
        # MENU
        # ============================================================
        # 'menu/',
        'views/backend/ob_menu.xml'

        # ============================================================
        # FUNCTION USED TO UPDATE DATA LIKE POST OBJECT
        # ============================================================
    ],

    'test': [],
    'demo': [],

    'installable': True,
    'active': False,
    'application': True,
}
