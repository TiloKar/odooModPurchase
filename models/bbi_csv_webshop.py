from odoo import api, fields, models, _
import csv, base64, sys, xlrd, io
from odoo.exceptions import ValidationError

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    csvdata = fields.Binary(String='CSV File')
    csvdata_file_name = fields.Char(String='Name')

    def csv_auslesen(self):
        result = self.env['product.supplierinfo'].search([('name', '=', self.partner_id.id)]) # product_supplierinfo partnerid gleich purchaseorder partnerid
        ausgabe = '' # Stringausgabe, die in die CSV eingetragen wird
        for j in self.order_line: # in der derzeitigen PurchaseOrderLine
            result = self.env['product.supplierinfo'].search([
                ('name', '=', self.partner_id.id), # Filtert alle Einträge aus Supplierinfo mit der gleichen Partner_id aus der PurchaseOrder
                ('product_tmpl_id', '=', j.product_id.product_tmpl_id.id), # Filtert alle Einträge aus Supplierinfo mit dem gleichen Produkt aus PurchaseOrderLine
                ('product_code', '!=', False)]) # Filtert alle Einträge die eine Artikelnummer beim Lieferanten besitzen
            if len(result) > 0:
                #Ausgabe für Artikelnummern die NICHT False sind
                ausgabe = ausgabe + str(int(j.product_qty)) + ';' + str(result[0].product_code)  + '\n' # Produktmenge + Artikelnummer (kurzbez. beim Lieferanten in Supplierinfo) "{:.0f}".format(sheet.cell(i, 1).value)
            else:
                #Ausgabe für Artikelnummern die False sind
                ausgabe = ausgabe + str(int(j.product_qty)) + ';' + 'unknown ' + j.name + '\n'

        raw = ausgabe.encode(encoding='utf-8', errors='replace') # String encoden
        self.csvdata = base64.b64encode(raw) # binärcode mit b64 encoden
        self.csvdata_file_name = str(self.name) + '.csv' # Name und Format des Downloads
