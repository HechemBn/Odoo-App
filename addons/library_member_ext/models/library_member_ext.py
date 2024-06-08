from odoo import models, fields

class LibraryMemberExt(models.Model):
    _inherit = 'library.member'
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')],
        string='Gender',
        required=True
    )
    etat_civil = fields.Selection(
        [('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced'), ('widowed', 'Widowed')],
        string='Marital Status',
        required=True
    )
