import scrapy
import csv
from scrapy import Request

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

# path_to_start_urls = "C:\\Users\\kmuth\\fyp-tutorial-redo\\datacollection\\hospital-links.csv"

class MySpider(scrapy.Spider):
  name = 'MySpider'
  # start_urls = get_start_urls(path_to_start_urls)

  def start_request(self):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
    request = Request(url = self.start_urls, callback = self.parse, headers=headers)
    yield request

  def parse(self, response):

    name = response.xpath('//*[@class="hospital notranslate"]/text()').get()
    try: 
      streetAddress = response.xpath('//*[@class="pad clear"]/div//span[2]/span/text()').get()
      addressLocality = response.xpath('//*[@class="pad clear"]/div//span[2]/span[2]/text()').get()
      addressRegion = response.xpath('//*[@class="pad clear"]/div//span[2]/span[3]/text()').get()
      postalCode = response.xpath('//*[@class="pad clear"]/div//span[2]/span[4]/text()').get()
    except:
      streetAddress = "not found"
      addressLocality = "not found"
      addressRegion = "not found"
      postalCode = "not found"

    try:
      href = "https://www.nhs.uk" + response.xpath('//*[@class="review-ratings-tabs"]/span/a/@href').get()
    except:
      href = "not found"

    url = response.url

    yield {
      'name' : name,
      'streetAddress' : streetAddress,
      'addressLocality' : addressLocality,
      'addressRegion' : addressRegion,
      'postalCode' : postalCode,
      'href' : href,
      'overview' : url
    }



