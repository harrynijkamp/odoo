from odoo import models, fields

class SalesOrde (models.Model):
    _inherit = "sales.order"

    short_note = fields.Char(string='Short Note')