# -*- encoding: utf-8 -*-
##############################################################################
#
#    Donation module for OpenERP
#    Copyright (C) 2014 Artisanat Monastique de Provence
#                       (http://www.barroux.org)
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
    'name': 'Donation Tax Receipt',
    'version': '0.1',
    'category': 'Accounting & Finance',
    'license': 'AGPL-3',
    'summary': 'Manage tax receipts for donations',
    'description': """
Donation Tax Receipt
====================

This module handles tax receipt for donations. It has been designed for France, but it should probably work (with some adaptations) for other countries.

It has been developped by brother Bernard and brother Irenee from Barroux Abbey and by Alexis de Lattre from Akretion.
    """,
    'author': 'Barroux, Akretion',
    'website': 'http://www.barroux.org',
    'depends': ['donation'],
    'data': [
        'donation_tax_view.xml',
        'donation_tax_data.xml',
        'partner_view.xml',
        'product_view.xml',
        'security/ir.model.access.csv',
        'wizard/tax_receipt_print_view.xml',
        'wizard/tax_receipt_annual_create_view.xml',
        ],
    'demo': [],
    'active': False,
}
