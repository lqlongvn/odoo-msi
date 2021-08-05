from odoo import fields, models, api

# customer (id, name, phone, address, gender - gan gender mac dinh la male)

class Customer(models.Model):
    _name = 'customer1'

    name = fields.Char(string='Tên khách hàng')
    phone = fields.Char(string='Điện thoại')
    address = fields.Char(string='Địa chỉ')
    gender = fields.Char(string='Giới tính', default='male')

    @api.model
    def create(self, vals):
        vals['name'] = vals['name'].title()
        record = super(Customer, self).create(vals)
        return record

    def write(self, vals):
        vals['name'] = vals['name'].title()
        result = super(Customer, self).write(vals)
        return result


