from odoo import models, fields

class ResPartner (models.Model):
    _inherit = "res.partner"

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender')