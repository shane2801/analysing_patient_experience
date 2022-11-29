import scrapy
from scrapy import Request
from ..items import ReviewscraperItem
from scrapy.selector import Selector
import csv

def get_start_urls(path):
  start_urls = []
  with open(path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for line in csv_reader:
      start_urls.append(line[10])
  print("Start urls found: ", len(start_urls))
  return start_urls


class HospitalReviewSpider(scrapy.Spider):
  name = 'get-hospital-reviews-spider'
  start_urls = get_start_urls(path="C:\\Users\\kmuth\\fyp-tutorial-redo\\datacollection\\data\\hospitals-masterfile.csv")
  # start_urls = get_gps_starturls(GPS_PATH) ## also change export path to a different folder to distinguish between gps jsons and hospitals jsons
  def start_request(self):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
    request = Request(url = self.start_urls, callback = self.parse, headers=headers)
    yield request

  def parse(self, response):
    items = ReviewscraperItem()
    for products in response.xpath('//div[@aria-label="Organisation review"]'):
      # start_url = response.request.url
      name = products.xpath('//*[@id="page-heading"]/span/span/text()').get()
      date = products.css('span.nhsuk-body-s::text').get()
      rating = products.css('p.nhsuk-u-visually-hidden::text').get()
      review = products.css('p.comment-text::text').get()

    
      items['name'] = name
      items['hospital'] = response.url.split("/")[5]
      items['date'] = date.replace("Posted on ", "")
      items['rating'] = rating
      items['review'] = review
      temp_url = response.url
      if "?" in temp_url:
        items['start_url'] = temp_url.split("?")[0]
      else:
        items['start_url'] = response.url
        
      yield items

    # handle pagination
    exist = Selector(text=response.body).xpath("//li[contains(concat(' ', @class, ' '), ' nhsuk-pagination-item--next ')]")
    if exist:
      next_page =  response.css('a.nhsuk-pagination__link.nhsuk-pagination__link--next').attrib['href']
      if next_page is not None:
        yield response.follow(next_page, callback=self.parse)
