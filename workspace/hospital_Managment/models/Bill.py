from odoo import fields,models,api

class HospitalBill(models.Model):
	_name = 'hospital.bill'
	_description = 'Hospital Bill'
	_rec_name = 'patient_id'


	patient_id = fields.Many2one(comodel_name='hospital.patient',required=True,string='Patient')
	visit_charge = fields.Integer(string='Visit Charge',default=500)
	medicines_charge = fields.Integer(compute='compute_charge',string='Medicines Charge')
	lab_charge = fields.Integer(string='Labtest Charge',compute='compute_charge')
	total_amount  = fields.Integer(string='Total',compute='compute_charge')



	@api.depends('patient_id')
	def compute_charge(self):
		total = 0
		charge = 0 
		for rec in self:
			res = self.env['hospital.prescription'].search([('patient_id.name','=',rec.patient_id.name)])
			for med in res.medicines_ids:
				total+=med.price
			rec.medicines_charge=total		
			for test in res.lab_test_ids:
				charge+=test.price
			rec.lab_charge = charge

		self.total_amount =  self.medicines_charge+self.lab_charge+self.visit_charge 


