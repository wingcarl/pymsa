import scrapy
import datetime
from testbot.items import TestbotItem


class QuotesSpider(scrapy.Spider):
    name = "weather"
    start_urls = [
        'http://www.zjg121.com/zjgqxj2/QXXX/Page/YuBao.aspx',
    ]

    def parse(self, response):
        weather_info = response.css('#iscroll::text').extract()
        str_weather = ''.join(weather_info)
        str_weather = str_weather.replace('\r','')
        item = TestbotItem()
        item['weather_detail'] = str_weather.encode().decode()
        item['add_time'] = datetime.datetime.now()
        p = item.save()
