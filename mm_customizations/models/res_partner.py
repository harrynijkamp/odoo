from odoo import models, fields

class ResPartner (models.Model):
    _inherit = "res.partner"

    my_field = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='My Field')