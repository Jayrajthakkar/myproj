from odoo import fields, models,api
from datetime import date


class HospitalPrescription(models.Model):
	_name="hospital.prescription" # table name.
	_description="Hospital Prescription"


	patient_id =fields.Many2one(comodel_name="hospital.patient",string="Patient") 
	medicines_ids= fields.Many2many(comodel_name='hospital.pharma',string='Medicines')
	doctor=fields.Char(compute="doctor_name",string='Doctor')	
	

	def doctor_name(self):
		for rec in self:
			data = self.env['hospital.appointment'].search([('patient_id.name','=',rec.patient_id.name)])
			rec.doctor = data.doctor
			
	
	
	
	