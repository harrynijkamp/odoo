from odoo import models, fields

class BasePartner (models.Model):
    _inherit = "res.partner"
    _inherit = ["mail.thread"]

    gender = fields.Selection([('male', 'Male'),('female', 'Female')], string='Gender', tracking=True)