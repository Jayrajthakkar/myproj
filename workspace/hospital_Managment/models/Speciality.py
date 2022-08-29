from odoo import fields, models,api
from datetime import date

class Speciality(models.Model):
	_name="hospital.speciality" #table name.
	_description="speciality"

	name=fields.Char(string='Speciality')     