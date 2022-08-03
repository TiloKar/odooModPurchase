from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

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

    def generateSupplierRef(self):
        if self.ref is False:
            result = self.env['res.partner'].search([('supplier_rank', '!=', False)])
            highest= 0
            try:
                for i in result:
                    if int(i.ref) > highest:
                        highest = int(i.ref)
            except:
                raise ValidationError ('Lieferantennummer beim Kontakt ' + i.name + ' überarbeiten!' )

            highest=highest+1
            return super(models.Model,self).write({'ref' : str(highest)})
