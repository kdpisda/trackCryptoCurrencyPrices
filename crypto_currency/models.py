from django.db import models
from profiles.models import Profile

# Create your models here.
class CurrencyPrices(models.Model):
	# Prices in INR
	CRYPTOCURRENCIES_CHOICES = (
			('BTC', 'BitCoin'),
			('ETH', 'Ethereum'),
			('LTC', 'Litecoin'),
		)
	currency = models.CharField(
			max_length=3,
			choices=CRYPTOCURRENCIES_CHOICES
		)
	last_tracked_price = models.FloatField()
	recorded_time = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		# TypeCasting to float
		self.last_tracked_price = float(self.last_tracked_price)
		super(CurrencyPrices, self).save(*args, **kwargs)

	def __str__(self):
		return self.currency + " at " + str(self.recorded_time)

class PriceAlerts(models.Model):
	CHANGE_CHOICES = (
			('UP', 'Up'),
			('DN', 'Down'),
		)
	user = models.ForeignKey(
			Profile,
			default=1,
			on_delete=models.CASCADE
		)
	notification_on_rate = models.FloatField(default=0)
	notification_criteria = models.CharField(
			max_length=2,
			choices=CHANGE_CHOICES
		)
	def __str__():
		return self.user.username