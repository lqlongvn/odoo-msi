from odoo import fields, models, api

class Customer(models.Model):
    _name = 'customer'

    id = fields.Integer(string='Customer ID')
    name = fields.Char(string='Tên Khách hàng')
    phone = fields.Char(string='Phone')
    add = fields.Char(string='Address')
    gender = fields.Char(string='Giới tính', default="male")

    order_ids = fields.One2many(comodel_name='orders', inverse_name='customer_id', string='Orders')
    customer_order_count = fields.Integer(compute='get_order_count', string='Count', store=False)

    @api.depends('order_ids')
    def get_order_count(self):
        for customer in self:
            customer.customer_order_count = len(customer.order_ids)
        return customer.customer_order_count

    @api.model
    def create(self, vals):
        vals['name'] = vals['name'].title()
        record = super(Customer, self).create(vals)
        return record

    def write(self, vals):
        vals['name'] = vals['name'].title()
        result = super(Customer, self).write(vals)
        return result

