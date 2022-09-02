from odoo import fields, models,api
from datetime import date


class HospitalPrescription(models.Model):
	_name="hospital.prescription" # table name.
	_description="Hospital Prescription"
	_rec_name = 'patient_id'


	patient_id =fields.Many2one(comodel_name="hospital.patient",string="Patient") 
	medicines_ids= fields.Many2many(comodel_name='hospital.pharma',string='Medicines')
	doctor=fields.Char(compute="doctor_name",string='Doctor')
	medicines_count = fields.Char(compute='_compute_medicines_count', string = 'Medicines Count')
	lab_test_ids = fields.Many2many(comodel_name='hospital.labtest',string='Medical Test')


	def doctor_name(self):
		for rec in self:
			data = self.env['hospital.appointment'].search([('patient_id.name','=',rec.patient_id.name)])
			rec.doctor = data.doctor

	def _compute_medicines_count(self):
		medicines_count=0
		for rec in self:
			rec.medicines_count = len(rec.medicines_ids.ids)

		
	def action_view_medicinescount(self):
		return{
		'name':"Medicines",
		'type':'ir.actions.act_window',
		'res_model':'hospital.pharma',
		'domain':[('id','=',self.medicines_ids.ids)],
		'view_mode':'tree,form',
		'target':'current'	

		}