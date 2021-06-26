from odoo import fields, models, api

class Employee(models.Model):
    _name = 'employee'

    name = fields.Char(string='Tên nhân viên')
    active = fields.Boolean(default=True, string='Active')
    state = fields.Selection(
        selection=[('0', 'Dang Lam Viec'), ('1', 'Nghi Thai San'), ('2', 'Nghi Phep'), ('3', 'Nghi Viec')],
        string='State')

    # def active_deactive(self):
    #     self.active = not self.active

    def leave(self):
        self.state = '1'

    def work(self):
        self.state = '0'
