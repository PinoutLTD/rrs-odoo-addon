from odoo import fields, models

class RRSRegister(models.Model):
    _name = "rrs.register"
    _description = "Robonomics Report Service Register"

    address = fields.Char(string="Address in Robonomics parachain", required=True)
    customer_email = fields.Char(string="Email")
    status = fields.Many2one(
        comodel_name="rrs.register.status",
        string="Status",
        help="Status indicates wheter the subscribtion was bought, not paid or expired",
    )
    started_date = fields.Datetime()
    expired_date = fields.Datetime()
    pinata_key = fields.Char(string="Pinata Key")
    pinata_secret = fields.Char(string="Pinata Secret")
