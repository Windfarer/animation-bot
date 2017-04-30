# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AnimationCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_name = scrapy.Field()
    tt_id = scrapy.Field()
    characters = scrapy.Field()
