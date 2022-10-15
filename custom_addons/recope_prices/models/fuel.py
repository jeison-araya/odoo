from odoo import fields, models

class Fuel(models.Model):
    _name = "fuel"

    name = fields.Char('Fuel name', required=True, translate=True)
    price = fields.Float('Price', required=True)

    _sql_constraints = [
        ('check_price', 'CHECK(price >= 0)', 'The price can\'t be negative.'),
    ]