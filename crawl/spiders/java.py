# -*- coding: utf-8 -*-
import scrapy


class JavaSpider(scrapy.Spider):
    name = 'java'
    allowed_domains = ['http://gawron.sdsu.edu/python_for_ss/course_core/book_draft/web/web_intro.html' , 'https://www.freetutorials.us/']
    start_urls = ['http://gawron.sdsu.edu/python_for_ss/course_core/book_draft/web/web_intro.html' , 'https://www.freetutorials.us/']

    def parse(self, response):
        h1 = response.xpath('//h1')
        h2 = response.xpath('//*[@class="logo-wrap"]/a')
        yield {'H1': h1 , 'H2': h2}
