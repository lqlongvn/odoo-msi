from odoo import fields, models, api

# products (name, description, date, price)

class Products(models.Model):
    _name = 'product2'

    name = fields.Char(string='Tên product')
    description = fields.Char(string='Mô tả product')
    product_date = fields.Date(string='Ngày của product')
    product_price = fields.Integer(string='Giá của product')

    orderline_ids = fields.One2many(comodel_name='orderline2', inverse_name='product_id', string='Order Line')