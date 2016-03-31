# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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
    'name': 'Human Resources And Payroll Reporting',
    'version': '1.1',
    'author': 'Gaurav Sahu',
    'category': 'Human Resources',
    'sequence': 22,
    'website': 'https://github.com/gauravsahu',
    'summary': 'Jobs, Departments, Employees Details and Payroll Reporting',
    'description': """
Human Resources & Payroll Reporting
==========================
    """,
    'depends': [
        'base','hr','hr_holidays','hr_payroll','hr_contract','hr_attendance','holiday_calendar'
    ],
    'data': [
        'hr_reporting_view.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}