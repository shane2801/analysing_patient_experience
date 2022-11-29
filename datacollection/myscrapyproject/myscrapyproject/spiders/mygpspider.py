import scrapy
from scrapy import Request
import csv


path_to_start_urls = "" # path to file
# read start urls from csv file that we scraped earlier using Selenium
def get_start_urls(path):
  start_urls = []
  with open(path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for line in csv_reader:
      start_urls.append(line[1])
  print("Start urls found: ", len(start_urls))
  return start_urls

class MyGPSpider(scrapy.Spider):
  name= 'myGpSpider'
  start_urls = get_start_urls(path = path_to_start_urls)
  # start_urls = [
  #   "https://www.nhs.uk/services/gp-surgery/abbey-dale-medical-centre/X39771"
  # ]

  def start_request(self):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
    request = Request(url = self.start_urls, callback = self.parse, headers=headers)
    yield request

  def parse(self, response):

    name = response.xpath('//*[@id="page-heading"]/span/span/text()').get().strip()
    addresses = response.xpath('//*[@id="address_panel_address"]/text()').getall()
    address = ''
    for temp_address in addresses:
      address +=  temp_address.strip()  + ", "

    try:
      google_link = response.xpath('//*[@id="address_panel_google_map_link"]/@href').get()
    except:
      google_link = "not found"

    try:
      href = "https://www.nhs.uk" + response.xpath('//*[@id="quick_link_href_ratings_reviews"]/@href').get()
    except:
      href = "not found"

    url = response.url

    yield {
      'name' : name,
      'address' : address,
      'google_link' : google_link,
      'href' : href,
      'overview' : url
    }

