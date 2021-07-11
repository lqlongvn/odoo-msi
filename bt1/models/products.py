from odoo import fields, models, api

class Products(models.Model):
    _name = 'products'

    name = fields.Char(string='Product Name')
    description = fields.Char(string='Description')
    price = fields.Integer(string='Price')
    date = fields.Datetime(string='Date')

    order_line_ids = fields.One2many(comodel_name='order_line', inverse_name='products_id', string='Order Line')

