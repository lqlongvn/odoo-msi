from odoo import fields, models, api

# customer (id, name, phone, address, gender - gan gender mac dinh la male)

class Customer(models.Model):
    _name = 'customer2'

    name = fields.Char(string='Tên khách hàng')
    phone = fields.Char(string='Điện thoại')
    address = fields.Char(string='Địa chỉ')
    gender = fields.Char(string='Giới tính', default='male')

    order_ids = fields.One2many(comodel_name='order1', inverse_name='customer_id', string='Orders')

