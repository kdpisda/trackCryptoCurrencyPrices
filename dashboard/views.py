from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'core/home.html')

def live_prices(request):
	return render(request, 'core/live_price.html')