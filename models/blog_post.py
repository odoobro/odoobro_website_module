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

from odoo import models, fields


class BlogPost(models.Model):

    _inherit = "blog.post"

    description_website = fields.Text(string="Description",
                                      help="Description show on website")
    link_odoo_app = fields.Char(string="Link",
                                help="Link on Odoo app")
    icon = fields.Binary(string="Icon",
                         help="Icon show on website",
                         attachment=True)
