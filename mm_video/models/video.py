from odoo import api, fields, models, _
from odoo.exceptions import ValidationError 

class Video(models.Model):
    _name = "metafoormedia.video"
    _inherit = ["mail.thread"]
    _description = "Vimeo Videos"

    name = fields.Char(string='Name', required=True, tracking=True)
    vimeo_link = fields.Char(string='Vimeo link', required=True, tracking=True) 

    project_id = fields.Many2one('project.project', string='Project', tracking=True)

    def get_player(self):
        for rec in self:
            if rec.vimeo_link == "":
                raise ValidationError(_("Vimeo link is empty"))