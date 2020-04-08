from odoo import models, fields, api

class Book(models.Model):
    _name = 'book'
    _description = 'This will contain all the book information'

    @api.depends('price')
    def _set_category(self):
        for rec in self:
            if rec.price >= 500:
                rec.category = 'high'
            elif rec.price < 500 and rec.price >=250:
                rec.category = 'normal'
            else:
                rec.category = 'low'

    name = fields.Char(string='Book Name', max_lngth=100, required=True)
    author = fields.One2many('author', 'book_name', string='Author Name')
    editor = fields.Char(string='Editors', max_length=100)
    edition = fields.Char(string='Edition', max_length=50)
    isbn = fields.Char(string='ISBN Number', max_length=50)
    image = fields.Binary(sring='Photo')
    price = fields.Float(string='Price', digits=(4,2))
    category = fields.Selection([
        ('high', 'Elite'), ('normal', 'Normal'), ('low', 'Low Grade')
    ], compute='_set_category')
    total_copy = fields.Integer(string='Total Copies')
