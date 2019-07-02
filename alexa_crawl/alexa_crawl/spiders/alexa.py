# -*- coding: utf-8 -*-
import scrapy
import csv
import os


class AlexaSpider(scrapy.Spider):
    name = 'alexa'
    allowed_domains = ['alexa.com']
    start_urls = ['http://alexa.com/']

    def start_requests(self):
        """Read domains from domains file and construct the search URL"""

        with open(os.path.join(os.path.dirname(__file__), "./resources/domains.csv")) as search_domains:
            for keyword in csv.reader(search_domains):
                try:
                    search_text = keyword[0]
                except:
                    search_text = ""
                    print("No domain found")

                url = "https://www.alexa.com/siteinfo/{0}".format(
                    search_text)
                yield scrapy.Request(url, callback = self.parse, meta = {"search_text": search_text})

    def parse(self, response):
        """Function to process alexa country demograph"""
        search_domain = response.meta["search_text"]
        country = response.xpath("//div[@class='visitorList']")

        for countries in country:

            XPATH_COUNTRYFIRST_NAME = ".//div[@id='countryName']/text()"
            XPATH_COUNTRYFIRST_PERCENT = ".//div[@id='countryPercent']/text()"
            XPATH_COUNTRYSECOND_NAME = ".//div[@id='countryName']/text()"
            XPATH_COUNTRYSECOND_PERCENT = ".//div[@id='countryPercent']/text()"

            raw_countryfname = country.xpath(XPATH_COUNTRYFIRST_NAME).extract()
            raw_countryfpercent = country.xpath(XPATH_COUNTRYFIRST_PERCENT).extract()
            raw_countrysname = country.xpath(XPATH_COUNTRYSECOND_NAME).extract()
            raw_countryspercent = country.xpath(XPATH_COUNTRYSECOND_PERCENT).extract()

            # cleaning the data

            country_fname = ''.join(raw_countryfname[0]).strip() if raw_countryfname else None
            country_fperent = ''.join(raw_countryfpercent[0]).strip() if raw_countryfpercent else None
            country_sname = ''.join(raw_countrysname[1]).strip() if raw_countrysname else None
            country_visit_second = ''.join(raw_countryspercent[1]).strip() if raw_countryspercent else None

            yield {
                'First Country': country_fname,
                'First Country %': country_fperent,
                'Second Country': country_sname,
                'Second Country %': country_visit_second,
            }
        
        return True