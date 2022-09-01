from odoo import fields, models,api
from datetime import date


class HospttalLabtest(models.Model):
	_name = 'hospital.labtest'
	_description = 'Hospital Medical tests'



	name = fields.Char(string='Medical tests')
	
	price = fields.Integer(string='Rate')


