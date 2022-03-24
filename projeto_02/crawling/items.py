import scrapy
from scrapy.contrib.djangoitem import DjangoItem
from main.models import Url_Scraper

class Url_Busca(DjangoItem):
    django_model = Url_Scraper
    u_urls = scrapy.Field()
    urls = scrapy.Field()
