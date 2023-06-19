from odoo import models, fields

class Project (models.Model):
    _inherit = "project.project"

    video_line_ids = fields.One2many('metafoormedia.video', 'project_id', string="Videos")
