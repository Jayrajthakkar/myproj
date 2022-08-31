from odoo import fields, models,api
from datetime import date


class HospitalPrescription(models.Model):
	_name="hospital.prescription" # table name.
	_description="Hospital Prescription"


	patient_id =fields.Many2one(comodel_name="hospital.patient",string="Patient") 
	medicines_ids= fields.Many2many(comodel_name='hospital.pharma',string='Medicines')
	doctor=fields.Char(compute="doctor_name",string='Doctor')
	appointment_count = fields.Char(compute='_compute_count',string="Count")
	patient_count = fields.Char(compute='_compute_patient_count',string="Count")


	def doctor_name(self):
		for rec in self:
			data = self.env['hospital.appointment'].search([('patient_id.name','=',rec.patient_id.name)])
			rec.doctor = data.doctor
	
	def _compute_count(self):
		for rec in self:
			res = self.env['hospital.appointment'].search_count([('patient_id.name','=',rec.patient_id.name)])
			self.appointment_count = res

	def _compute_patient_count(self):
		for rec in self:
			res = self.env['hospital.patient'].search_count([('name','=',rec.patient_id.name)])
			self.patient_count = res		
	
	
	def action_view_appointmentcount(self):
		return{
		'name':"Appointment",
		'type':'ir.actions.act_window',
		'res_model':'hospital.appointment',
		'domain':[('patient_id.name','=',self.patient_id.name)],
		'view_mode':'tree,form',
		'target':'current'	

		}

	def action_view_patientcount(self):
		return{
		'name':"Patient",
		'type':'ir.actions.act_window',
		'res_model':'hospital.patient',
		'domain':[('name','=',self.patient_id.name)],
		'view_mode':'tree,form',
		'target':'current'	

		}