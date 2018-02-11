from django.contrib import admin
from .models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
	"""docstring for ProfileAdmin"""
	list_display = ('user', 'bio')
	icon = '<i class="material-icons">account_circle</i>'
	
admin.site.register(Profile, ProfileAdmin)