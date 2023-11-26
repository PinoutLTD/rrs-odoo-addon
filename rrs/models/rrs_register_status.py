from odoo import fields, models


class RRSRegisterStatus(models.Model):

    _name = "rrs.register.status"
    _description = "Robonomics Report Service Register Status"
    _order = "sequence, id"
    name = fields.Char(required=True)
    sequence = fields.Integer(default=10)
