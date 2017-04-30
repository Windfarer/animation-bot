# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import AnimationCrawlerItem

list_base_url = "http://www.imdb.com/search/title{}"
credits_url_template = "http://www.imdb.com{}"

regex = re.compile(r'\([^)]*\)')

class ImdbSpider(scrapy.Spider):
    name = "imdb"
    allowed_domains = ["www.imdb.com"]
    start_urls = ["http://www.imdb.com/search/title?genres=animation&title_type=feature&sort=moviemeter,asc&page=1&ref_=adv_nxt"]
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        'COOKIES_ENABLES': False
    }

    def parse(self, response):
        tt_list = response.xpath('//*[@id="main"]/div/div/div[3]/div/div[3]/h3/a/@href').extract()

        for tt in tt_list:
            credits_url = credits_url_template.format(tt.split('?')[0])
            yield scrapy.Request(url=credits_url, callback=self.parse_credits)

        next_page_params = response.xpath('//a[@class="lister-page-next next-page"]/@href').extract_first()
        if next_page_params:
            yield scrapy.Request(url=list_base_url.format(next_page_params))

    def parse_credits(self, response):
        characters = set()
        movie_name = response.xpath('//meta[@property="og:title"]/@content').extract_first()
        tt_id = response.xpath('//meta[@property="pageId"]/@content').extract_first()

        matched = response.xpath('//td[@class="character"]/div')
        for i in matched:
            collection = []
            for part in i.xpath('.//text()').extract():
                p = re.sub(regex, '', part)
                p = p.replace('\n', '').replace('Additional Voices', '')
                p = " ".join(p.split())
                if p:
                    collection.append(p)
            names = [name.strip() for name in "".join(collection).split('/') if name.strip()]
            characters.update(names)

        yield AnimationCrawlerItem(movie_name=movie_name,
                                   tt_id=tt_id,
                                   characters=list(characters))