from odoo import api, fields, models

class SupplierInfo(models.Model):
    _inherit = 'product.supplierinfo'
    #tauscht die supplierinfo in der reihenfolge, LEGACY
    def action_open_make_standard(self):
        if self._context.get('sequence_action_clicked_id'):
            me = self.env['product.supplierinfo'].search([('id','=',self._context.get('sequence_action_clicked_id')),])
            toSwap = self.env['product.supplierinfo'].search([('product_tmpl_id','=',me.product_tmpl_id.id),('sequence','=',1)])
            if len(toSwap) > 0:
                tmp=me.sequence
                print("swapping {} - {}".format(me.sequence,toSwap[0].sequence))
                me.update({'sequence' : 1})
                toSwap[0].update({'sequence' : tmp})

    #auto fill nummern vomm lieferanten in product-supplier tab bei änderung
    def compMySupplierInfo(self,s):
        if (s.product_tmpl_id.id == self.product_tmpl_id.id) and \
        (s.name.id == self.name.id) and \
        (s.id != self.id) and \
        ((s.product_code == False) or (s.product_code == '')) : return True
        return False

    #auto fill nummern vomm lieferanten in product-supplier tab bei änderung
    #@api.onchange('product_code')
    @api.constrains('product_code')
    def _autoFill(self):
        unfilled  = self.env['product.supplierinfo'].search([]).filtered(lambda s: self.compMySupplierInfo(s))
        print(unfilled)
        if ((self.product_code != False) and (self.product_code != '')) and (len(unfilled) > 0 ):
            for s in unfilled:
                s.update({'product_code' : self.product_code})
