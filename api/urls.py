from django.conf.urls import url, include
from . import views as api_views

urlpatterns = [
    url(r'^get_price/', api_views.get_live_price),
    url(r'^get_updated_price/', api_views.get_current_price),
]