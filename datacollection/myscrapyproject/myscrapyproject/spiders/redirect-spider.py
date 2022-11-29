import scrapy
from scrapy import Request
import json
from scrapy.utils.python import to_unicode
from urllib.parse import urlparse
import urllib
from scrapy.item import Item, Field
import csv


all_hospitals_links = "C:\\Users\\kmuth\\fyp-tutorial-redo\\datacollection\\data\\all-hospitals-links.csv"

# read start urls from csv file that we scraped earlier using Selenium - hospitals
def get_start_urls_for_hospitals(path):
  start_urls = []
  with open(path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for line in csv_reader:
      start_urls.append(line[1])
  print("Start urls found: ", len(start_urls))
  return start_urls

# read start urls from csv file that we scraped earlier using Selenium-gps
# def get_start_urls_for_gps(path):
#   start_urls = []
#   with open(path, 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     next(csv_reader)
#     for line in csv_reader:
#       start_urls.append(line[1])
#   print("Start urls found: ", len(start_urls))
#   return start_urls

class BrokenItem(Item):
    url = Field()
    starturl = Field()
    status = Field()

class RedirectSpider(scrapy.Spider):
  name = "redirect_parser_spider"
  handle_httpstatus_list = [301,302]
  # we first need add the urls to start urls
  start_urls = get_start_urls_for_hospitals(path=all_hospitals_links)
  def parse(self, response):
    item = BrokenItem()
    tempurl = response.url
    if response.status >= 300 and response.status < 400:
      # HTTP header is ascii or latin1, redirected url will be percent-encoded utf-8
      location = to_unicode(response.headers['location'].decode('latin1'))
      # get the original request
      request = response.request
      # and the URL we got redirected to
      redirected_url = urllib.parse.urljoin(request.url, location)
      item['url'] = redirected_url
      item['starturl'] = tempurl
      yield item

    else:  
      yield item