from django.shortcuts import render
from django.http import JsonResponse
from crypto_currency.models import CurrencyPrices
# from django.conf import settings
# from django.utils.timezone import activate
# activate(settings.TIME_ZONE)

# Create your views here.
def get_live_price(request):
	response = {}
	time_slab = []
	price_history = {}
	co_ordinates = []
	
	temp_currency_prices = CurrencyPrices.objects.filter(currency="BTC")
	for temp_currency_price in temp_currency_prices:
		temp_co_ordinates = temp_currency_price.last_tracked_price
		time_slab.append(str(temp_currency_price.recorded_time.strftime("%d/%m/%y %H:%M")))
		co_ordinates.append(temp_co_ordinates)
	price_history['BTC'] = co_ordinates
	co_ordinates = []
	
	temp_currency_prices = CurrencyPrices.objects.filter(currency="ETH")
	for temp_currency_price in temp_currency_prices:
		temp_co_ordinates = temp_currency_price.last_tracked_price
		co_ordinates.append(temp_co_ordinates)
	price_history['ETH'] = co_ordinates
	co_ordinates = []
	
	temp_currency_prices = CurrencyPrices.objects.filter(currency="LTC")
	for temp_currency_price in temp_currency_prices:
		temp_co_ordinates = temp_currency_price.last_tracked_price
		co_ordinates.append(temp_co_ordinates)
	price_history['LTC'] = co_ordinates

	response['success'] = True
	response['price'] = price_history
	response['time'] = time_slab
	return JsonResponse(response)

def get_current_price(request):
	response = {}
	temp_prices = {}
	currency_price = CurrencyPrices.objects.filter(currency="BTC").latest('recorded_time')
	temp_prices['BTC'] = currency_price.last_tracked_price
	time_stamp = currency_price.recorded_time.strftime("%d/%m/%y %H:%M")
	currency_price = CurrencyPrices.objects.filter(currency="ETH").latest('recorded_time')
	temp_prices['ETH'] = currency_price.last_tracked_price
	currency_price = CurrencyPrices.objects.filter(currency="LTC").latest('recorded_time')
	temp_prices['LTC'] = currency_price.last_tracked_price
	response['success'] = True
	response['time'] = time_stamp
	response['data'] = temp_prices
	return JsonResponse(response)