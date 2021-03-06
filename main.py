# coding: utf-8

from quokka.core.app import QuokkaModule
from .views import DonationView, TransactionListView
from .functions import get_random_campaign, get_latest_donations

module = QuokkaModule("fundraising", __name__, template_folder="templates")

module.add_app_template_global(get_random_campaign)
module.add_app_template_global(get_latest_donations)

module.add_url_rule('/fundraising/donate/',
                    view_func=DonationView.as_view('donate'))

module.add_url_rule('/fundraising/transactions/',
                    view_func=TransactionListView.as_view('transactions'))
