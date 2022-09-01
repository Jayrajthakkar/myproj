from odoo import fields,models,api

class HospitalBill(models.Model):
	_name = 'hospital.bill'
	_description = 'Hospital Bill'


	patient_id = fields.Many2one(comodel_name='hospital.patient',required=True,string='Patient')
	visit_charge = fields.Integer(string='Visit Charge',default=500)
	medicines_charge = fields.Integer(string='Medicines Charge')
	# total_amount  = fields.Char()



	@api.onchange('patient_id')
	def onchange_charge(self):
		total = 0
		for rec in self:
			res = self.env['hospital.prescription'].search([('patient_id.name','=',rec.patient_id.name)])
			data = self.env['hospital.pharma'].search([('id','=',res.medicines_ids.ids)])
			
			for meds in data:
				print(meds.price)
				total+=meds.price

			rec.medicines_charge=total