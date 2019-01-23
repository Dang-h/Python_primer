import scrapy
from firstspider.items import CourseItem
from scrapy.seletor import Selector

class FirstSpider(scrapy.Spider):
    name = "myfirstSpider"
    allowed_domains = ["shiyanlou.com"]
    start_urls = ['https://www.shiyanlou.com/courses/?category=all&course_type=all&tag=all&fee=free']

    def parse(self, response):
        hxs = Seletor(response)
        course = hxs.xpath('//div[@class="col-md-3 col-sm-6 course"]')
        for course in courses:
            item = CourseItem()
            item['name'] = course.xpath('.//div[@class="course-name"]/text()').extract()[0].strip()
            item['learned'] = course.xpath('.//span[@class="course-per-num pull-left"]/text()').extract()[1].strip()
            item['image'] = course.xpath('.//div[@class="course-ima"]/ima/@src').extract()[0].strip()
            yield item
