from odoo import fields, models,api
from datetime import date

class SpecialityDoctors(models.Model):
	_name="hospital.doctor" # table name.
	_description="Doctor"

	name=fields.Char(string='Name')
	age =fields.Integer(string='Age')
	speciality_ids=fields.Many2one(comodel_name='hospital.speciality',string='Speciality')
	patients_count=fields.Char(compute="_compute_patients_count",string="Patient")

	def _compute_patients_count(self):
		for rec in self:
			# rec.patients_count = 0
			patient = self.env['hospital.appointment'].search_count([('speciality_id.name','=',rec.speciality_ids.name)])
			# print("===================================...................>>>>>>>>",patient)
			rec.patients_count=patient 		