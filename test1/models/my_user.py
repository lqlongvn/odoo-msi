from odoo import fields, models, api

class My_User(models.Model):
    _name = 'myuser'
    _inherit = "res.users"
    # _inherit = "employees1"
    _description = "Extend res_users model"


