import time
import math
import random
from openerp.osv import fields, osv
from openerp.tools.translate import _
from datetime import datetime ,timedelta
from dateutil.relativedelta import relativedelta
from tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT
import xlwt
from xlwt import Workbook, XFStyle, Borders, Pattern, Font, Alignment,  easyxf
import cStringIO
import base64, urllib

    

class hr_reporting(osv.osv_memory):
    _name = 'hr.reporting'
    _columns = {
        'employee_id': fields.many2one('hr.employee','Employee', size=32, domain="[('active','in',['false','true'])]" ),
        'holiday_list_id': fields.many2one('holiday.list','Months', size=32, ),
        'date': fields.date("Date",),
        'by_month': fields.boolean('By Month'),
        'address_ids': fields.many2many('res.partner', 'res_partner_group_rel', 'report_id', 'address_id', 'Working Address'),
        'address_id' : fields.many2one('res.partner','Working Address'),
        'category': fields.selection([('worker','Worker'),('staff','Staff'),('contractor','Contractor')], 'Category'),
        'export_data':fields.binary('File',readonly=True),
        'filename':fields.char('File Name',size=250,readonly=True), 
        'report_type':fields.selection([('salary_report','Salary Report')], 'Report Type'),         
    }