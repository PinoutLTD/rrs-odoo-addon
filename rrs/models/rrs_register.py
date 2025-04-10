from odoo import fields, models


class RRSRegister(models.Model):
    _name = "rrs.register"
    _description = "Robonomics Report Service Register"
    _inherit = ['mail.thread']

    address = fields.Char(string="Subscription controller address in Robonomics parachain", required=True)
    customer_email = fields.Char(string="Email")
    paid = fields.Boolean(string="Is a service paid or free", default=False)
    last_paid = fields.Datetime()
    pinata_key = fields.Char(string="Pinata Key")
    pinata_secret = fields.Char(string="Pinata Secret")
    revolut_cid = fields.Char(string="Revolut customer id")
    revolut_order_id = fields.Char(string="Revolut last order id")
