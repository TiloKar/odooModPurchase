from odoo import api, fields, models, _

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    supplier_extrainfo = fields.Char('Steuernr. Finanzamt',
        help='bbi_steuernr_finanzamt',
        store=True,
        readonly=False)

    supplier_our_id_customer = fields.Char('Kundennummer vom Lieferanten',
        help='bbi_Kundennummer_vom_Lieferanten',
        store=True,
        readonly=False)
