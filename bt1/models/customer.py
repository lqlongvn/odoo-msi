from odoo import fields, models, api

class Customer(models.Model):
    _name = 'customer'

    id = fields.Integer(string='Customer ID')
    name = fields.Char(string='Tên Khách hàng')
    phone = fields.Char(string='Phone')
    add = fields.Char(string='Address')
    gender = fields.Char(string='Giới tính', default="male")

    customer_count = fields.Integer(compute='get_customer_count', string='Count', store=True)

    # @api.depends('order_line_ids')
    def get_customer_count(self):
        pass
        return True
        # for order in self:
            # print(order.order_ids[0].customer_id)
            # order.customer_count = 8
            # order.customer_count = len(order.order_line_ids)

    @api.model
    def create(self, vals):
        vals['name'] = vals['name'].title()
        record = super(Customer, self).create(vals)
        return record

    def write(self, vals):
        vals['name'] = vals['name'].title()
        result = super(Customer, self).write(vals)
        return result

