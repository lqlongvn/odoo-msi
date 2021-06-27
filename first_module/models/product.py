
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

class Product(models.Model):
    _name = 'product'

    def get_default_purchase_date(self):
        return datetime.now()


    name = fields.Char(string='Name', required=True)
    price = fields.Integer(string='Sale Price')
    purchase_date = fields.Datetime(string='Purchase Date', default=get_default_purchase_date)
    warranty = fields.Selection(selection=[('warranty', 'Warranty'), ('not', 'Not Warranty')], string='Warranty')
    vat = fields.Float(default=0.1, string='Thuế VAT')
    price_with_tax = fields.Float(string='Price with Tax', compute='get_price_with_tax')
    active = fields.Boolean(string='Active', default=True)
    category_id = fields.Many2one(comodel_name='product.categories', string ='Category')
    # category_id = fields.Many2one('product.categories', 'Category')
    supplier_ids = fields.Many2many(comodel_name='supplier', relation='supplier_product_rel', column1='product_id',
                                    column2='supplier_id', string='Suppliers')


    @api.depends('vat', 'price')
    def get_price_with_tax(self):
        for product in self:
            if product.vat:
                product.price_with_tax = product.price + (product.price * product.vat)
            else:
                product.price_with_tax = product.price

    @api.model
    def create(self, vals):
        vals['name'] = vals['name'].title()
        record = super(Product, self).create(vals)
        return record


    @api.constrains('price')
    def validate_price(self):
        if not self.price or self.price <= 0:
            raise ValidationError('Price need greater than 0!')

    def write(self, vals):
        result = super(Product, self).write(vals)
        return result

    def unlink(self):
        return super(Product, self).unlink()

    @api.onchange('price')
    def onchange_price(self):
        if self.price and self.price > 10:
            self.warranty = 'warranty'
        else:
            self.warranty = 'not'
