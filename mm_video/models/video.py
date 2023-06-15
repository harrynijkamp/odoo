from odoo import api, fields, models, _
from odoo.exceptions import ValidationError 

class Video(models.Model):
    _name = "metafoormedia.video"
    _inherit = ["mail.thread"]
    _description = "Vimeo Videos"

    name = fields.Char(string='Name', required=True, tracking=True)
    vimeo_link = fields.Char(string='Vimeo link', required=True, tracking=True) 
    project_id = fields.Many2one('project.project', string='Project', required=True, tracking=True)
    partner_count = fields.Integer(string='Partner', compute='_compute_partner_id')

    def _compute_partner_id(self):
        partner_count = self.env['project.project'].search_count([('partner_id', '=', self.id)])
        self.partner_count = partner_count

