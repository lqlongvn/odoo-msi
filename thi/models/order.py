from odoo import fields, models, api
from odoo.exceptions import ValidationError

# model order (customer_id, order_date, total_amount=sum(line.sub_total), order_ids)

class Order(models.Model):
    _name = 'order1'

    name = fields.Char(string='Tên đơn hàng')
    order_date = fields.Date(string='Ngày đơn hàng')


    state = fields.Selection(
        selection=[('0', 'Draft'), ('1', 'Doing'), ('2', 'Done'), ('3', 'Cancel order')],
        string='Trạng thái')

    def unlink(self):
        if self.state != '2':
            return super(Order, self).unlink()
        else:
            raise ValidationError('Order already Done, cannot be deleted!')
