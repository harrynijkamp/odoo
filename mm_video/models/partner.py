from odoo import models, fields

class Partner (models.Model):
    _inherit = "res.partner"

    video_ids = fields.Many2many('metafoormedia.video', 'video_partner_rel', 'video_id', 'partner_id', string='Video Involvement')
    gen = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender')