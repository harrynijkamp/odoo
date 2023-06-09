from odoo import models, fields

class SaleOrde (models.Model):
    _inherit = "sale.order"

    short_note = fields.Char(string='Short Note')