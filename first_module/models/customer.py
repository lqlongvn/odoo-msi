from odoo import fields, models, api

class Customer(models.Model):
    _name = 'customerfirst'

    name = fields.Char(string='Tên Customer')
