#from website_sale.controllers.main import table_compute

__author__ = 'openerp'
from openerp import fields, models, api
from openerp.http import request
import datetime
import random
from dateutil.relativedelta import relativedelta
from openerp.osv import osv
from openerp.tools.translate import _


class Auctions(models.Model):
    """Auctions class called"""

    _name = 'auction.edit'
    _description = 'Parameters of auctions'

    def get_default_datetime_now(self):
        now = fields.Datetime.now()
        return now

    def get_count_days(self):
        format_dt = '%Y-%m-%d'
        start = datetime.datetime.strptime(self.start_auction_date_time, format_dt)
        end = datetime.datetime.strptime(self.stop_auction_date_time, format_dt)
        diff = relativedelta(end, start)
        self.days = int(diff.days)

    @api.onchange('minimum_bid')
    def check_end_date_auction(self):
        if self.stop_auction_date_time == fields.Date.today():
            self.is_active = False

    @api.one
    @api.constrains('start_auction_date_time', 'stop_auction_date_time')
    def check_field_dates_rights(self):
        if self.start_auction_date_time > self.stop_auction_date_time:
            raise Warning('Start date must not be earlier than the End date')
        elif self.start_auction_date_time == self.stop_auction_date_time:
            raise Warning('Nothing to perform, please set correct date and time')

    @api.onchange('products')
    def check_fields_duplicates(self):
        uid, cr, pool, context = request.uid, request.cr, request.registry, request.context
        for id in pool.get('auction.edit').search(cr, uid, []):
            if self.products.id == pool.get('auction.edit').browse(cr, uid, id, []).products.id:
                #name = self.products.name
                #message = "The product %s is used, please set other product" % name
                self.products = ''
                #self.modal_window('', message)

    def modal_window(self, title, message):
        raise osv.except_osv(_(title), _(message))

    is_active = fields.Boolean(default=True, help="Sets the status of the auction")
    auction_name = fields.Char(string="Name auctions", required=True, help="The name of auction")
    start_auction_date_time = fields.Date(string="Start date and time", default=get_default_datetime_now, required=True, help="Default now date and time, The field should not be later 'Stop date auction'")
    stop_auction_date_time = fields.Date(string="End date and time", required=True, help="The field should not be before 'Start date auction'")
    days = fields.Integer(compute=get_count_days, readonly=True)
    minimum_bid = fields.Float(string="Minimum bet", required=True)
    products = fields.Many2one('product.product', 'price', required=True, help="Select a product or create a new product. The field is require")
    step = fields.Float(default=1, help="The field set step between bets")

    description_auction = fields.Text(string="Auction Description", help="The not require field, but need for informational")


class Bits(models.Model):
    """Bits class called"""

    _name = 'like.bits'
    _description = 'Parameters of bits'

    u_bit = fields.Float(string='Bet', readonly=True, default=0)
    user_name = fields.Char(string='User name', readonly=True, default='User')
    date_bit = fields.Datetime(string='Date bit', readonly=True, default='')
    product = fields.Char(string="Product name", readonly=True)
    user_id = fields.Integer()
    product_id = fields.Integer()


class Finished_auctions(models.Model):

    _name = 'finish.auctions'

    auction_finish = fields.Many2one('auction.edit', 'auction_name', readonly=True)
    user_win = fields.Many2one('res.users', readonly=True)
    user_bet = fields.Float(readonly=True)
    product = fields.Char(readonly=True)
    description = fields.Text()









