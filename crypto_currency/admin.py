from django.contrib import admin
from .models import CurrencyPrices

# Register your models here.
class CurrencyPricesAdmin(admin.ModelAdmin):
	list_display = ('currency', 'last_tracked_price', 'recorded_time')
	icon = '<i class="material-icons">attach_money</i>'

admin.site.register(CurrencyPrices, CurrencyPricesAdmin)