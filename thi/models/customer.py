from odoo import fields, models, api

class ToDoList(models.Model):
    _name = 'customer1'

    name = fields.Char(string='Tên khách hàng')
