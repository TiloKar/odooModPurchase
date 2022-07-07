from odoo import api, fields, models

class SupplierInfo(models.Model):
    _inherit = 'product.supplierinfo'

    def action_open_make_standard(self):
        print("was mit sequenzen")
