from odoo import models, fields

class ResPartner (models.Model):
    _inherit = "res.partner"
    _inherit = ["mail.thread"]

    my_field = fields.Selection([
        ('value1', 'Label 1'),
        ('value2', 'Label 2'),
        ('value3', 'Label 3')
    ], string='My Field', tracking=True)