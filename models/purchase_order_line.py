from odoo import api, fields, models, _

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    product_code = fields.Char(
        string = 'Artikelnr. beim Lief.',
        help='Bestellnummer beim Lieferanten',
        store=True,
        readonly=False,)

    # überschreibt das automatische Belegen des beschreibugsfeldes mit Lieferanten-bestellnr
    def _get_product_purchase_description(self, product_lang):
        self.ensure_one()

        seller = self.product_id.with_company(1)._select_seller(
            partner_id=self.partner_id,
            quantity=self.product_uom_qty,
            date=self.order_id.date_order and self.order_id.date_order.date(),
            uom_id=self.product_id.uom_po_id)

        if seller:
            if seller.product_code:
                self.product_code = seller.product_code

        #name = product_lang.display_name
        name=""
        if product_lang.name:
            name = product_lang.name
        name += " "
        if product_lang.description_purchase:
            name += '\n' + product_lang.description_purchase

        return name
