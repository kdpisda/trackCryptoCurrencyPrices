from django.conf import settings
from .models import CurrencyPrices
from django_cron import CronJobBase, Schedule
import datetime
import requests

class UpdateCryptoCurrencyPricesCronJob(CronJobBase):
    """
    CRON job to update price from API and store it in database
    """
    RUN_EVERY_MINS = 0 if settings.DEBUG else 20   # 20 minutes when not DEBUG

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'cron.UpdateCryptoCurrencyPricesCronJob'

    def do(self):
        message = 'Updating price at : %s' % str(datetime.datetime.now().time())
        get_price = requests.get('https://koinex.in/api/ticker')
        temp_prices = get_price.json()
        new_price = CurrencyPrices.objects.create(
                currency = 'BTC',
                last_tracked_price = temp_prices['prices']['BTC']
            )
        new_price.save()
        new_price = CurrencyPrices.objects.create(
                currency = 'ETH',
                last_tracked_price = temp_prices['prices']['ETH']
            )
        new_price.save()
        new_price = CurrencyPrices.objects.create(
                currency = 'LTC',
                last_tracked_price = temp_prices['prices']['LTC']
            )
        new_price.save()
        print(message)