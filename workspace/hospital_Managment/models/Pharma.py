from odoo import fields, models,api
from datetime import date


class HospitalPharma(models.Model):
	_name="hospital.pharma" # table name.
	_description="Hospital Pharma"


	name = fields.Char(string='Medicines')
	manufacturer = fields.Char(string='Manufacturer')
	manufacturer_site = fields.Char(string='Manufacturer Website')
	medicines_stock = fields.Integer(string='Available Stock')
