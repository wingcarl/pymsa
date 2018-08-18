import scrapy
import datetime
from testbot.items import WindScrapyItem


class QuotesSpider(scrapy.Spider):
    name = "windscrapy"
    start_urls = [
        'http://www.zjg121.com/zjgqxj2/QXXX/GetInfo.ashx?title=weather&infotype=FS&station=%E9%95%BF%E6%B1%9F%E9%98%B2%E6%B1%9B%E5%A4%84',
    ]

    def parse(self, response):
        weather_info = response.css('#iscroll::text').extract()
        str_weather = ''.join(weather_info)
        str_weather = str_weather.replace('\r','')
        item = TestbotItem()
        item['weather_detail'] = str_weather.encode().decode()
        item['add_time'] = datetime.datetime.now()
        p = item.save()
