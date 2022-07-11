from datetime import datetime, time
from dateutil.relativedelta import relativedelta
from functools import partial
from itertools import groupby
import json

from markupsafe import escape, Markup
from pytz import timezone, UTC
from werkzeug.urls import url_encode

from odoo import api, fields, models, _
from odoo.osv import expression
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools.float_utils import float_compare, float_is_zero, float_round
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.tools.misc import formatLang, get_lang, format_amount

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    bbi_vendor_confirmation_date = fields.Datetime('Lief. Bestätigungsdatum',
        help='Das Datum, an der Lieferant die Bestellung bestätigt hat - AB',
        store=True,
        readonly=False)

    def _prepare_supplier_info(self, partner, line, price, currency):
        # Prepare supplierinfo data when adding a product
        # EDIT_Hanning Liu
        # min_qty wird auf line.product_qty gesetzt, fixxt die 0 in der Einkaufsübersicht
        # ergänzung tk sequence swap, damit letzter einkaufsvorgang default wird

        toSwap = self.env['product.supplierinfo'].search([('product_tmpl_id','=',line.product_id.product_tmpl_id.id),('sequence','=',1)])
        if len(toSwap) > 0:
            newSeq = max(line.product_id.seller_ids.mapped('sequence')) + 1 if line.product_id.seller_ids else 1
            print("changing sequnce supplierinfo {} to {}".format(toSwap[0].id,newSeq))
            toSwap[0].update({'sequence' : newSeq})

        return {
            'name': partner.id,
            #'sequence': max(line.product_id.seller_ids.mapped('sequence')) + 1 if line.product_id.seller_ids else 1,
            'sequence': 1,
            'min_qty': line.product_qty,
            'price': price,
            'currency_id': currency.id,
            'delay': 0,
            }

    def _add_supplier_to_product(self):
        # Add the partner in the supplier list of the product if the supplier is not registered for
        # this product. We limit to 10 the number of suppliers for a product to avoid the mess that
        # could be caused for some generic products ("Miscellaneous").
        for line in self.order_line:
            # Do not add a contact as a supplier
            partner = self.partner_id if not self.partner_id.parent_id else self.partner_id.parent_id
            # EDIT_Hanning_Liu
            # Bedingung wird rausgenommen, sodass gleiche Lieferanten aufgezählt werden. Zusätzlich wird die Anzeigebedingung von 10 Zeilen ausgehoben
            if line.product_id:
                # Convert the price in the right currency.
                currency = partner.property_purchase_currency_id or self.env.company.currency_id
                price = self.currency_id._convert(line.price_unit, currency, line.company_id, line.date_order or fields.Date.today(), round=False)
                # Compute the price for the template's UoM, because the supplier's UoM is related to that UoM.
                if line.product_id.product_tmpl_id.uom_po_id != line.product_uom:
                    default_uom = line.product_id.product_tmpl_id.uom_po_id
                    price = line.product_uom._compute_price(price, default_uom)

                supplierinfo = self._prepare_supplier_info(partner, line, price, currency)
                # In case the order partner is a contact address, a new supplierinfo is created on
                # the parent company. In this case, we keep the product name and code.
                seller = line.product_id._select_seller(
                    partner_id=line.partner_id,
                    quantity = line.product_qty,
                    date=line.order_id.date_order and line.order_id.date_order.date(),
                    uom_id=line.product_uom)
                if seller:
                    supplierinfo['product_name'] = seller.product_name
                    supplierinfo['product_code'] = seller.product_code
                #bbi mod:       neue productcodes hier übernehmen
                if line.product_code:
                    supplierinfo['product_code'] = line.product_code

                vals = {
                    'seller_ids': [(0, 0, supplierinfo)],
                }
                try:
                    line.product_id.write(vals)
                except AccessError:  # no write access rights -> just ignore
                    break
