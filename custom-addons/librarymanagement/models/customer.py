from odoo import models, fields


class Customer(models.Model):
    _name = 'customer'
    _description = 'Customer Information'
    _rec_name = 'first_name'

    first_name = fields.Char(string='First Name', require=True)
    last_name = fields.Char(string='Last Name')
    phone = fields.Char(string='Phone Number')
    email = fields.Char(string='Email')
    address = fields.Char(string='Address')
    image = fields.Binary()