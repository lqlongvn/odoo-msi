from odoo import fields, models, api

# customer (id, name, phone, address, gender - gan gender mac dinh la male)

class Customer(models.Model):
    _name = 'customer3'

    name = fields.Char(string='Tên khách hàng')
    phone = fields.Char(string='Điện thoại')
    address = fields.Char(string='Địa chỉ')
    gender = fields.Char(string='Giới tính', default='male')
