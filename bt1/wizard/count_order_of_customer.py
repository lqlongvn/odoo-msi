from odoo import fields, models, api

class CountOrderOfCustomer(models.TransientModel):
    _name = 'count.order'

    count_order_of_customer = fields.Integer(string='Số lượng order của Customer', default=0)

    def get_order_count(self):
        customer_id = self.env.context.get('active_id', False)
        customer_record = self.env['customer'].browse(customer_id)
        count_order_of_customer= customer_record.customer_order_count
        return count_order_of_customer