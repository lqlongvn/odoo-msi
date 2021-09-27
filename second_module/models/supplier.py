from odoo import models, fields, api

class Supplier(models.Model):
    # _name = 'supplier_inherit'
    _inherit = 'supplier'

    address = fields.Text(string='Address')
    phone = fields.Char(string='Phone')

