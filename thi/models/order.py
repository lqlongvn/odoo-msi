from odoo import fields, models, api
from odoo.exceptions import ValidationError

class Order(models.Model):
    _name = 'order1'

    name = fields.Char(string='Tên đơn hàng')
    order_date = fields.Char(string='Ngày đơn hàng')


    state = fields.Selection(
        selection=[('0', 'Draft'), ('1', 'Doing'), ('2', 'Done'), ('3', 'Cancel order')],
        string='Trạng thái')

    def unlink(self):
        if self.state != '2':
            return super(Order, self).unlink()
        else:
            raise ValidationError('Order already Done, cannot be deleted!')
