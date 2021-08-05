from odoo import fields, models, api

# order_line (order_id, product_id, created_date, qty, amount, sub_total=qty * amount)

class OrderLine(models.Model):
    _name = 'orderline1'

    name = fields.Char(string='Tên order_line')
    created_date = fields.Date(string='Ngày đơn hàng')
    qty = fields.Integer(string='Số lượng')
    unit_price = fields.Integer(string='Đơn giá')
    thanhtien = fields.Integer(string='Thành tiền', compute='get_thanhtien', store=True)

    @api.depends('qty', 'unit_price')
    def get_thanhtien(self):
        for product in self:
            product.thanhtien = product.qty * product.unit_price

