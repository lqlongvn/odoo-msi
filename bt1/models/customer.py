from odoo import fields, models, api

class Customer(models.Model):
    _name = 'customer'

    id = fields.Integer(string='Customer ID')
    name = fields.Char(string='Tên Khách hàng')
    phone = fields.Char(string='Phone')
    add = fields.Char(string='Address')
    gender = fields.Char(string='Giới tính', default="male")

    @api.model
    def create(self, vals):
        vals['name'] = vals['name'].title()
        record = super(Customer, self).create(vals)
        return record

    def write(self, vals):
        vals['name'] = vals['name'].title()
        result = super(Customer, self).write(vals)
        return result

