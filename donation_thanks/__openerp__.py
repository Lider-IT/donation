# -*- encoding: utf-8 -*-
##############################################################################
#
#    Donation Thanks module for OpenERP
#    Copyright (C) 2014 Abbaye du Barroux
#    @author Alexis de Lattre <alexis.delattre@akretion.com>
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
    'name': 'Donation Thanks',
    'version': '0.1',
    'category': 'Accounting & Finance',
    'license': 'AGPL-3',
    'summary': 'Create thanks letter for a donation',
    'description': """
Donation Thanks
===============

This module adds a report on a donation to create a thanks letter. The thanks letter is generated in ODT format, so you need to have LibreOffice on your desktop.

It has been developped by brother Bernard and brother Irenee from Barroux Abbey and by Alexis de Lattre from Akretion.
    """,
    'author': 'Barroux, Akretion',
    'website': 'http://www.barroux.org',
    'depends': ['donation', 'report_aeroo'],
    'data': [
        'report_thanks.xml',
        'donation_view.xml',
        ],
    'demo': [],
    'active': False,
}
