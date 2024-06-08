from odoo import models, fields

class LibraryCheckoutExt(models.Model):
    _inherit = 'library.checkout'
    emprint = fields.Char(
        string='emprint'
    )
