from odoo import fields, models,api
from datetime import date

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
			a = "success"
		else:
			a = "warning"

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


		