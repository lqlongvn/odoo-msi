from odoo import models, fields, api

class Supplier(models.Model):
    _name = 'supplier'

    name = fields.Char(string='Supplier Name', required=True)
    description = fields.Char(string='Mô tả Nhà cung cấp')

    @api.model
    def create(self, vals):
        vals['name'] = vals['name'].title()
        record = super(Supplier, self).create(vals)
        return record
