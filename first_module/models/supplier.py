from odoo import models, fields, api

class Supplier(models.Model):
    _name = 'supplier'

    name = fields.Char(string='Supplier Name', required=True)
    description = fields.Char(string='description')
    # name = fields.Char()
    product_ids = fields.Many2many(comodel_name='product', relation='supplier_product_rel', column1='supplier_id',
                                   column2='product_id', string='Products')
    # product_ids = fields.Many2many('product', string='Products')

