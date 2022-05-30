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
  ],
  'data': [
    'views/res_partner_supplier_extrainfo_view.xml',
  ],
}
