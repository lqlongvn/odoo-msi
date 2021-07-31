from odoo import fields, models, api

class EmployeeLeaveReason(models.TransientModel):
    _name = 'count.order'

    count_order_of_customer = fields.Integer(string='Số lượng order của Customer', default=5)
