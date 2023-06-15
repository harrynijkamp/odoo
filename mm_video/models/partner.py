from odoo import models, fields

class Partner (models.Model):
    _inherit = "res.partner"

    video_involvement_line_ids = fields.One2many('metafoormedia.video', 'id', string="Involved")