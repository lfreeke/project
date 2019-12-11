# -*- coding: utf-8 -*-
from odoo import fields, models


class ProjectDecision(models.Model):
    _name = 'project.decision'
    _inherit = 'mail.thread'
    _order = 'decision_date'

    project_id = fields.Many2one(
        'project.project', string='Project')
    sequence = fields.Integer(default=1)
    decision_date = fields.Date()
    decision_summary = fields.Char()
    decision_log = fields.Html()
    agreed_by_customer = fields.Boolean(track_visibility='onchange')
    agreed_by_pm = fields.Boolean(track_visibility='onchange')
