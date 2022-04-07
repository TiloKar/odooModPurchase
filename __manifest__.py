# -*- coding: utf-8 -*-
# bbi Customisation für Freitextnotizen in Angebotspositionen
# @author: Tilo K
# @date:    April 2022
# Version 1.0 Webshopeigenschaft an product_template, Positionsfreitext im angebot vom Produkt

{
  'name': 'bbi mod purchase',
  'version': '1.0',
  'category': 'Purchase',
  'description': """
     verändert Methode _add_supplier_to_product Methode, sodass alle Einkäuf eingetragen werden
    """,
  'depends': [
    'base',
    'purchase',
  ],
  'data': [
  ],
}
