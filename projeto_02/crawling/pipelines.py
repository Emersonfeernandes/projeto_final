from main.models import Url_Scraper

def clean_url(param):
    return param
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


class CrawlingPipeline(object):
    def process_item(self, item, spider):
        url = clean_url(item['link'])

        Movie.objects.create(
            url=url
        )

        return item
