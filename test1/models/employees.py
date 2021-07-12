from odoo import fields, models, api

class Employees(models.Model):
    _name = 'employees1'

    name = fields.Char(string='Name')
    active = fields.Boolean(default=True, string='Active')
    state = fields.Selection(
        selection=[('0', 'Dang Lam Viec'), ('1', 'Nghi Thai San'), ('2', 'Nghi Phep'), ('3', 'Nghi Viec')], string='State')

    def work(self):
        pass

    # Biến và Hàm cho Smart Button
    employees_count = fields.Integer(compute='get_employees_count', string='SL Nhân viên', store=True)
    def get_employees_count(self):
        self.employees_count = 8
        pass




