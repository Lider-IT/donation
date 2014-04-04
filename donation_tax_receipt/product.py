# -*- encoding: utf-8 -*-
##############################################################################
#
#    Donation module for OpenERP
#    Copyright (C) 2014 Barroux Abbey
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

from openerp.osv import orm, fields


class product_template(orm.Model):
    _inherit = 'product.template'

    _columns = {
        'tax_receipt_ok': fields.boolean(
            'Is Eligible for a Tax Receipt',
            help="Specify if the product is eligible for a tax receipt"
            "in a donation line."),
        }
