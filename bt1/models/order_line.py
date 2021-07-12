from odoo import fields, models, api

class Order_line(models.Model):
    _name = 'order_line'

    # order_id = fields.Integer(string='Order ID')
    # product_id = fields.Integer(string='Product ID')
    order_id = fields.Many2one('orders', string='Order')
    products_id = fields.Many2one('products', string ='Product')

    created_date = fields.Datetime(string='Created Date')
    qty = fields.Integer(string='Quantity')
    amount = fields.Integer(string='Amount')
    sub_total = fields.Integer(string='Sub Total')


