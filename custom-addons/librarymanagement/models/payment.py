import datetime
from odoo import models, fields, api


class Payment(models.Model):
    _name = 'book.payment'
    _details = 'This will contain payment info'
    _order = 'state desc'

    def action_pay(self):
        for rec in self:
            rec.state = 'paid'

    rental_ids = fields.One2many('book.rent', 'payment_ids')
    due_amount = fields.Float(digits=(4, 2))
    extra_charge = fields.Float(digits=(4, 2))
    total_amount = fields.Float(digits=(4, 2), compute='_cal_total', store=True, readonly=True)
    payment_date = fields.Datetime(string='Payment Date', default=datetime.datetime.now())
    customer_ids = fields.Many2one('customer', related='rental_ids.customer')
    state = fields.Selection([('unpaid', 'Unpaid'), ('paid', 'Paid')],
                             default='unpaid', readonly=True)

    @api.depends('due_amount', 'extra_charge')
    def _cal_total(self):
        for res in self:
            res.total_amount = res.due_amount + res.extra_charge
