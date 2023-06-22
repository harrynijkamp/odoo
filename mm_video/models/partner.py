from odoo import models, fields

class Partner (models.Model):
    _inherit = "res.partner"

    video_ids = fields.Many2many('metafoormedia.video', 'video_partner_rel', 'video_id', 'partner_id', string='Video Involvement')
    my_field = fields.Selection([
        ('value1', 'Label 1'),
        ('value2', 'Label 2'),
        ('value3', 'Label 3')
    ], string='My Field')
    