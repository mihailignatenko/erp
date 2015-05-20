__author__ = 'openerp'

from openerp import http
from openerp.http import request
from datetime import datetime
from openerp.addons.website.models import website





    #def set_auctions_tracker(self, add_qty=0, id=0, product_id=0, product='', date=''):

    #def set_defautl_qty(self):
    #     cr, uid, context, pool = request.cr, request.uid, request.context, request.registry
    #     quantity = lambda id: pool.get('auction.edit').browse(cr, uid, id, context=context).minimum_bid
    #     return http.request.render({'value': quantity(4)})