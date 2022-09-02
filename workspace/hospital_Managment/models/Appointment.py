from odoo import fields, models,api
from datetime import date

class Appointment(models.Model):
	_name="hospital.appointment" # table name.
	_description="Patient Appointment"
	_rec_name = 'patient_id'

	patient_id = fields.Many2one(comodel_name="hospital.patient",string="Patient")
	speciality_id=fields.Many2one(comodel_name='hospital.speciality',string='Speciality')
	doctor=fields.Char(string='Doctor')
	visit_charge = fields.Integer(string='Visit Charge',default=500)
	verify_patient= fields.Selection([('registered','Registered'),('unregistered','Unregistered')],string='Verify')
	patient_count = fields.Char(compute='_compute_patient_count',string="Petient Count")
	

	def _compute_patient_count(self):
		for rec in self:
			rec.patient_count = len(rec.patient_id.ids)


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


	def action_view_patientcount(self):
		return{
		'name':"Patient",
		'type':'ir.actions.act_window',
		'res_model':'hospital.patient',
		'domain':[('id','=',self.patient_id.ids)],
		'view_mode':'tree,form',
		'target':'current'	

		}		