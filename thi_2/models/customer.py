from odoo import fields, models, api

# customer (id, name, phone, address, gender - gan gender mac dinh la male)

class Customer(models.Model):
    _name = 'customer2'

    name = fields.Char(string='Tên khách hàng')
    phone = fields.Char(string='Điện thoại')
    address = fields.Char(string='Địa chỉ')
    gender = fields.Char(string='Giới tính', default='male')

    order_ids = fields.One2many(comodel_name='order2', inverse_name='customer_id', string='Orders')

    customer_order_count = fields.Integer(compute='get_order_count', string='Count', store=False)
    @api.depends('order_ids')
    def get_order_count(self):
        for customer in self:
            customer.customer_order_count = len(customer.order_ids)
        return customer.customer_order_count

