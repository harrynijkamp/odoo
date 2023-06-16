from odoo import models, fields

class Partner (models.Model):
    _inherit = "res.partner"

    video_involvement_line_ids = fields.Many2many('metafoormedia.video', 'partner_id', string="Involved")