from odoo import models, fields


class Rent(models.Model):
    _name = 'book.rent'
    _description = 'Book rental Description'

    book = fields.Many2many('book')
    customer = fields.Many2many('customer')
    rental_date = fields.Datetime(string='Rental Date')
    return_date = fields.Datetime(string='Return Date')