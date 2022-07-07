from odoo import api, fields, models

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    vendor_confirmation_date = fields.Datetime('Lief. Bestätigungsdatum',
        help='Das Datum, an der Lieferant die Bestellung bestätigt hat - AB',
        store=True,
        readonly=False)
