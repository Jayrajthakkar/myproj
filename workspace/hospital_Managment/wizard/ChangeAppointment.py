from odoo import fields, models,api

class ChangeAppointment(models.TransientModel):
	_name="change.appointment.wizard" # table name.
	_description="Change Appointment"
	#_rec_name = 'appointment_id'

	appointment_id = fields.Many2many(comodel_name="hospital.appointment",string="Patient")
	reason = fields.Char(string='Reason')


	def action_change(self):
		for rec in self:
			for val in rec.appointment_id:
				val.verify_patient = 'registered'

		return{
		'type':'ir.actions.act_window',
		'name':'Appointment',
		'res_model':'hospital.appointment',
		'view_mode':'tree,form',
		'target':'current'
		}
