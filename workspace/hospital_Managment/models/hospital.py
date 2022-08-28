from odoo import fields, models,api
from datetime import date

class Speciality(models.Model):
	_name="hospital.speciality" #table name.
	_description="speciality"

	name=fields.Char(string='Speciality')     

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

class City(models.Model):
	_name="hospital.city" #table name.
	_description="Hospital City"


	name=fields.Char(string='City')

class Appointment(models.Model):
	_name="hospital.appointment" # table name.
	_description="Patient Appointment"

	patient_id = fields.Many2one(comodel_name="hospital.patient",string="Patient")
	speciality_id=fields.Many2one(comodel_name='hospital.speciality',string='Speciality')
	doctor=fields.Char(string='Doctor')
	verify_patient= fields.Selection([('registered','Registered'),('unregistered','Unregistered')],string='Verify')
	
	def verify(self):
		res = self.verify_patient
		a =""
		message = 'Verification is: '+res
		if res == 'registered':
			a = "Verification successful"
		else:
			a = "Verification failed"

		return{
		'type':'ir.actions.client',
		'tag':'display_notification',
		'params':{
		'message':message,
		'type':a,
		'sticky':False
		}
		}
 

		
	@api.model
	def create(self,vals):
		res = super(Appointment,self).create(vals)
		if vals.get('speciality_id',False):  
			data = self.env['hospital.doctor'].search([('speciality_ids.name','=',res.speciality_id.name)])
			res.doctor = data.name
		 
		return res 


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
