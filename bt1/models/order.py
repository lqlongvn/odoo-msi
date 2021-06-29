from odoo import fields, models, api

class Order(models.Model):
    _name = 'order'

    # customer_id = fields.Integer(string='Customer ID of Order')
    # customer_id = fields.Many2one('order', string='Customer')
    customer_id = fields.Many2one(comodel_name='customer', string='Customers')


    order_date = fields.Datetime(string='Order Date')
    total_amount = fields.Float(string='Total amount')

    # order_ids = fields.Integer(string='Order ids')
    # order_ids = fields.One2many(comodel_name='order_line', inverse_name='order_id', string='Lines')

    order_line_ids = fields.One2many(comodel_name='order_line', inverse_name='order_id', string='Lines')
    state = fields.Selection(
        selection=[('0', 'Dang thực hiện order'), ('1', 'Hủy bỏ order')],
        string='State')
    active = fields.Boolean(default=True, string='Active')


    customer_count = fields.Integer(compute='get_customer_count', string='Count', store=True)

    @api.depends('order_line_ids')
    def get_customer_count(self):
        for order in self:
            # print(order.order_ids[0].customer_id)
            # order.customer_count = 8
            order.customer_count = len(order.order_line_ids)



    def cancel_order(self):
        pass
        # self.active = not self.active