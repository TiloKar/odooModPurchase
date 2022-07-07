from odoo import api, fields, models

class SupplierInfo(models.Model):
    _inherit = 'product.supplierinfo'
    #tauscht die supplierinfo in der reihenfolge
    def action_open_make_standard(self):
        if self._context.get('sequence_action_clicked_id'):
            me = self.env['product.supplierinfo'].search([('id','=',self._context.get('sequence_action_clicked_id')),])
            toSwap = self.env['product.supplierinfo'].search([('product_tmpl_id','=',me.product_tmpl_id.id),('sequence','=',1)])
            if len(toSwap) > 0:
                tmp=me.sequence
                print("swapping {} - {}".format(me.sequence,toSwap.sequence))
                me.update({'sequence' : 1})
                toSwap.update({'sequence' : tmp})
