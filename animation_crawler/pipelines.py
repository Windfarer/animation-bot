# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from models import Animation
from mongoengine import connect
import os

class AnimationCrawlerPipeline(object):
    def __init__(self):
        connect('db', host=os.getenv("MONGO_URI", "mongodb://localhost/db"))

    def process_item(self, item, spider):
        Animation(**dict(item)).save()
        return item
