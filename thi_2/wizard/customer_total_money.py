from odoo import fields, models, api

class Customer_Total_Money(models.TransientModel):
    _name = 'customertotalmoney2'

    # customer_total_money = fields.Integer(string='Tổng số tiền của các đơn hàng của Customer', default='100')
    customer_total_money = fields.Integer(string='Tổng số tiền của các đơn hàng của Customer')
