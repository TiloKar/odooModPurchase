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
