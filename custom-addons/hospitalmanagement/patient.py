from odoo import models, fields, _, api


class HospitalPatients(models.Model):
    _name = 'hospital.patient'
    _description = 'Schema for Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name_seq'

    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    age = fields.Integer(string='Age', default=0)
    note = fields.Text(string='Note')
    image = fields.Binary(string='Image')
    name_seq = fields.Char(string='Patient serial', required=True, copy=False, readonly=True,
                       index=True, default='New')

    @api.model
    def create(self, vals_list):
        if vals_list.get('name_seq', 'New') == 'New':
            vals_list['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.seq') or 'New'
        result = super(HospitalPatients, self).create(vals_list)
        return result

    def write(self, vals):
        if vals.get('name_seq', 'New') == 'New':
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.seq') or 'New'
        result = super(HospitalPatients, self).write(vals)
        return result
