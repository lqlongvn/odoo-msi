
from odoo import models, fields, api

class Product_categories(models.Model):
    _name = 'product.categories'

    name = fields.Char(string='Product category Name', required=True)
    description = fields.Char(string='Mô tả Chủng loại')
    product_ids = fields.One2many(comodel_name='product', inverse_name='category_id', string='Product')
    product_count = fields.Integer(compute='get_product_count', string='Product Count', store=True)

    @api.depends('product_ids')
    def get_product_count(self):
        for category in self:
            print(category.product_ids[0].name)
            # category.product_count = 0
            category.product_count = len(category.product_ids)


    # @api.model
    # def create(self, vals):
    #     vals['name'] = vals['name'].title()
    #     record = super(Product_categories, self).create(vals)
    #     return record
    #

