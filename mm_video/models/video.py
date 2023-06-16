from odoo import api, fields, models, _
from odoo.exceptions import ValidationError 

class Video(models.Model):
    _name = "metafoormedia.video"
    _inherit = ["mail.thread"]
    _description = "Vimeo Videos"

    name = fields.Char(string='Name', required=True, tracking=True)
    vimeo_link = fields.Char(string='Vimeo link', required=True, tracking=True) 
    project_id = fields.Many2one('project.project', string='Project', required=True, tracking=True)
    partner_ids = fields.Many2many('res.partner', string='Involvement', tracking=True)
