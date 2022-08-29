from odoo import fields, models,api
from datetime import date




class City(models.Model):
	_name="hospital.city" #table name.
	_description="Hospital City"


	name=fields.Char(string='City')



class HospitalPatient(models.Model):
	_name="hospital.patient" # table name.
	_description="Hospital Patient"

	#the columns of the table.
	name = fields.Char(string='Name')
	age = fields.Integer(string='age',compute='_compute_age',store=True)
	birthdate = fields.Date(string='Birthdate')
	city_id = fields.Many2one(comodel_name='hospital.city',string='City')
	contact_number = fields.Char(string="Contact")
	details = fields.Char(string="Details")
	appointment_count = fields.Char(compute='_compute_count',string="Count")

	def _compute_count(self):
		for rec in self:
			res = self.env['hospital.appointment'].search_count([('patient_id','=',rec.id)])
			self.appointment_count = res	



	@api.model
	def create(self,vals):
		vals['details'] = vals['name'] + " , " + vals['contact_number']
		res = super(HospitalPatient,self).create(vals)
		return res 
	
	def write(self, vals):
		if self.name and self.contact_number:
			 
			vals['details'] = vals['name'] + " , " + vals['contact_number'] 
			res = super(HospitalPatient,self).write(vals)
			return res
		else:
			vals['details'] = vals['name'] + " , " + vals['contact_number']  
			res = super(HospitalPatient,self).write(vals)
			return res

	@api.depends('birthdate')
	def _compute_age(self):
		for rec in self:
			rec.age = 0
			if rec.birthdate:
				birthDate = rec.birthdate
				today = date.today()
				age = today.year - birthDate.year -((today.month, today.day) < (birthDate.month, birthDate.day))
 
				rec.age = age
	
	
	def unlink(self):
		"""Override method to unlink hospital references that is linked to patient"""
		for rec in self:
			hospital_Appointment = self.env['hospital.appointment'].search([('patient_id','=',rec.id)])
			res = super(HospitalPatient,self).unlink()
			hospital_Appointment.unlink()
			return res

	def action_view_patientcount(self):
		return{
		'name':"Appointment",
		'type':'ir.actions.act_window',
		'res_model':'hospital.appointment',
		'domain':[('patient_id','=',self.id)],
		'view_mode':'tree,form',
		'target':'current'

		}