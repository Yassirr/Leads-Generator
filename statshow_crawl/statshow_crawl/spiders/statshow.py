# -*- coding: utf-8 -*-
import scrapy
import csv
import os


class StatshowSpider(scrapy.Spider):
    name = 'statshow'
    allowed_domains = ['statshow.com']
    start_urls = ['http://statshow.com/']

    def start_requests(self):
        """Read domains from domains file and construct the search URL"""

        with open(os.path.join(os.path.dirname(__file__), "../resources/domains.csv")) as search_domains:
            for keyword in csv.reader(search_domains):
                try:
                    search_text = keyword[0]
                except:
                    search_text = ""
                    print('No domain found!')

                url = "http://www.statshow.com/www/{0}".format(
                    search_text)
                yield scrapy.Request(url, callback = self.parse, meta = {"search_text": search_text})

    def parse(self, response):
        """Function to process statshow search results page"""
        search_domain = response.meta["search_text"]
        stats = response.xpath("//div[@class='worth_left_box']")

        # iterating over search results
        for stat in stats:
            
            XPATH_MONTH_VISIT = ".//div[@id='box_2']/span[@class='red_bold']/text()"
            XPATH_MONTH_PAGEVIEW = ".//div[@id='box_2']//span[@class='red_bold']/text()"

            raw_month_visit = stat.xpath(XPATH_MONTH_VISIT).extract()
            raw_month_pageview = stat.xpath(XPATH_MONTH_PAGEVIEW).extract()

            # cleaning the data
            
            month_visit = ''.join(raw_month_visit[1]).strip() if raw_month_visit else None
            month_pageview = ''.join(raw_month_pageview[0]).strip() if raw_month_pageview else None

            yield {
                'search_text': search_domain,
                'month_visit': month_visit,
                'month_pageview': month_pageview
            }
