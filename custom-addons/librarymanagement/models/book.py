from odoo import models, fields

class Book(models.Model):
    _name = 'book'
    _description = 'This will contain all the book information'

    name = fields.Char(string='Book Name', max_lngth=100, required=True)
    author = fields.One2many('author', 'book_name', string='Author Name')
    editor = fields.Char(string='Editors', max_length=100)
    edition = fields.Char(string='Edition', max_length=50)
    isbn = fields.Char(string='ISBN Number', max_length=50)
    image = fields.Binary(sring='Photo')

