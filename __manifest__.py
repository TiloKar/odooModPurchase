# -*- coding: utf-8 -*-
# bbi Customisation für Freitextnotizen in Angebotspositionen
# @author: Tilo K
# @date:    April 2022
# Version 1.0 Webshopeigenschaft an product_template, Positionsfreitext im angebot vom Produkt

{
  'name': 'bbi_mod_purchase',
  'version': '1.2',
  'author': "Hanning Liu",
  'category': 'Purchase',
  'description': """
     - verändert Methode _add_supplier_to_product Methode, sodass alle Einkäuf eingetragen werden, märz 22
     - fügt zusätzliche Informationen zu res_partners hinzu, die im Kaufmann vorhanden waren, umgezogen aus supplier extrainfo mod im Mai 22
    """,
  'depends': [
    'base',
    'purchase',
    'purchase_stock',
  ],
  'data': [
    'views/bbi_csv_webshop.xml',
    'views/res_partner_supplier_extrainfo_view.xml',
    'views/purchase_order_form_bbi.xml',
    'views/purchase_order_tree_bbi.xml',
    'views/stock_picking_tree_bbi.xml',
    'views/stock_picking_form_bbi.xml',
    'views/product_template_form_supplier_bbi.xml',
    #'report/bbi_report_purchasequotation_document_erweiterung.xml',
    #'report/bbi_report_purchaseorder_document_erweiterung.xml',
    'report/minified_purchasequotation.xml',
    'report/minified_purchaseorder.xml',
    'report/bbi_report_purchasequotation.xml',
    'report/bbi_report_purchaseorder.xml',
    'report/change_paperformat.xml',
    'views/request_quotation_select_bbi.xml',
  ],
}
