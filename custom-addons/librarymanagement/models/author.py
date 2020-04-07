from odoo import models, fields

class Author(models.Model):
    _name = 'author'
    _description = 'This table will contain information about Author'
    _rec_name = 'first_name'

    first_name = fields.Char(string='First Name', max_length=100, required=True)
    last_name = fields.Char(string='Last Name', max_length=100)
    phone = fields.Char(string='Phone Number', max_length=25)
    email = fields.Char(string='Email', max_length=50)
    book_name = fields.Many2one('book')