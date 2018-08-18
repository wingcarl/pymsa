from django.conf.urls import url, include
from . import views
 
 
urlpatterns = [
url(r'add_wind$', views.add_wind, ),
url(r'show_wind$', views.show_wind, ),
url(r'show_water$', views.show_water, ),
url(r'show_weather$', views.show_weather, ),
url(r'add_wind_scrapy$', views.wind_check, ),
url(r'show_wind_scrapy$', views.show_wind_scrapy, ),
url(r'show_wind_level$', views.show_wind_level, ),
url(r'show_weather_alert$', views.show_weather_alert, ),
]
