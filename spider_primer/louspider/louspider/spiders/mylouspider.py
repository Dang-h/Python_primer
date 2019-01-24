import scrapy
from louspider.items import CourseItem
from scrapy.seletor import Selector

class LouSpider(scrapy, Spider):
    name = "myfirstspider"
    allowed_domains = ["shiyanlou.com"]
    start_urls = ['https://www.shiyanlou.com/courses/?category=all&course_type=all&tag=all&fee=frei']

    def parse(self, response):
        hxs = Selector(response)
        courses = hxs.xpath('//div[@class="col-md-3 col-sm-6  course"]')
        for course in courses:
            item = CourseItem()
            item['name'] = course.xpath('.//div[@class="course-name"]/text()').extract()[0].strip()
            item['learned'] = course.xpath('.//span[@class="course-per-num pull-left"]/text()').extract()[1].strip()
             item['image'] = course.xpath('.//div[@class="course-img"]/img/@src').extract()[0].strip()
             
             yield item
