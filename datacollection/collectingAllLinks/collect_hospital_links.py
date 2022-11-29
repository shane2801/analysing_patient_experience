from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv

url = "https://www.nhs.uk/Services/Pages/HospitalList.aspx"

service = ChromeService(executable_path=ChromeDriverManager().install())
options = ChromeOptions()
driver = webdriver.Chrome(options=options, service=service)
driver.get(url)

links = driver.find_elements(By.XPATH,'//*[@class="notranslate o-listing"]/a')
print("number of links found: ", len(links))


hrefs = []
texts = []
for link in links:
  # print("link: ", link)
  # print("href: ", link.get_attribute('href'))
  # print("text: ", link.text)
  href = link.get_attribute('href')
  text = link.text
  hrefs.append(href)
  texts.append(text)


print("hrefs: ", len(hrefs))
print("texts: ", len(texts))

print("Writing file...")

with open('hospital-links.csv', 'w', encoding='utf-8', newline='') as csvfile:
  # specify field names
  fieldnames = ['hospital name', 'link']
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  writer.writeheader()

  for id, text in enumerate(texts):
    writer.writerow({'hospital name': text, 'link': hrefs[id]})

print("Successfully found all the links")
