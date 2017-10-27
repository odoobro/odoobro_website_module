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

from odoo import http
from odoo.addons.website.controllers.main import Website
from odoo.http import request
import json


class OdoobroController(Website):

    @http.route('/', type='http', auth="public", website=True)
    def index(self, **kw):
        return http.request.render('odoobro_website_module.homepage', {})

    @http.route('/customer_question/<string:model_name>', type='http',
                auth="public", methods=['POST'], website=True)
    def customer_question(self, model_name, **kwargs):
        model_record = request.env['ir.model'].search(
            [('model', '=', model_name)])
        if not model_record:
            return json.dumps(False)
        try:
            values = dict(request.params)
            record = request.env[model_record.model].sudo().create(values)
        except IntegrityError:
            return json.dumps(False)
        return json.dumps({'id': record.id})
