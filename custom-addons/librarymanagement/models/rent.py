import datetime
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError


class Rent(models.Model):
    _name = 'book.rent'
    _description = 'Book rental Description'
    _order = 'return_date'

    @api.depends('book', 'return_date')
    def _set_due_price(self):
        for rec in self:
            if rec.return_date < datetime.datetime.now():
                rec.due_price = (datetime.datetime.now() - rec.return_date).days * (10)
            else:
                rec.due_price = 0

    def get_book_errors(self, all_books):
        errors = ''
        if all_books:
            for book in all_books:
                get_cur_book = self.env['book'].search([
                    ('id', '=', book)
                ])
                if get_cur_book.total_copy <= 0:
                    errors += get_cur_book.name + ' is not available.'
            return errors

    def action_rent(self):
        for rec in self:
            rec.state = 'rent'

    def action_returned(self):
        for rec in self:
            rec.state = 'return'


    @api.constrains('return_date')
    def _set_constraint(self):
        for rec in self:
            if rec.rental_date > rec.return_date:
                raise ValidationError(_('Return date cannot be past of rental date'))

    @api.model
    def create(self, vals):
        cur_book = vals.get('book', None)
        vals['state'] = 'draft'
        all_books = None
        if cur_book:
            all_books = cur_book[0][2]
        errors = self.get_book_errors(all_books)

        if errors:
            raise ValidationError(errors)
        else:
            for book in all_books:
                get_cur_book = self.env['book'].search([
                    ('id', '=', book)
                ])
                get_cur_book.write({
                    'total_copy': get_cur_book.total_copy - 1
                })

        result = super(Rent, self).create(vals)
        return result

    def write(self, vals):
        state = vals.get('state', None)
        cur_book = vals.get('book', None)
        all_books = []
        if state != 'rent':
            if cur_book:
                all_books = cur_book[0][2]
            errors = self.get_book_errors(all_books)
            if errors:
                raise ValidationError(errors)
            else:
                cur_book_ids = []
                for i in self.book:
                    cur_book_ids.append(i.id)
                if cur_book or state == 'return':
                    for book in self.book:
                        if book.id not in all_books:
                            book.write({
                                'total_copy': book.total_copy + 1
                            })

                for book in all_books:
                    if book not in cur_book_ids:
                        get_cur_book = self.book.search([('id', '=', book)])
                        get_cur_book.write({
                            'total_copy': get_cur_book.total_copy - 1
                        })
        result = super(Rent, self).write(vals)
        return result

    book = fields.Many2many('book', required=True)
    customer = fields.Many2one('customer', required=True)
    rental_date = fields.Datetime(string='Rental Date', default=datetime.datetime.now())
    return_date = fields.Datetime(string='Return Date', default=datetime.datetime.now() + datetime.timedelta(days=5))
    due_price = fields.Float(digits=(3,2), compute='_set_due_price')
    state = fields.Selection([('init','Init'),('draft', 'Draft'), ('rent', 'Rented'), ('return', 'Returned')],
                             default='init', readonly=True)
