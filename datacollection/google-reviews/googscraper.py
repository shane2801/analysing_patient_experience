from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.google.co.uk/maps/place/Airedale+General+Hospital/@53.8977439,-1.9663537,17z/data=!3m2!4b1!5s0x487bf1e304e93ff1:0xa2f430e4ecfc8e65!4m5!3m4!1s0x487bf1e3041694f3:0x2b0a6460592a104a!8m2!3d53.8977439!4d-1.964165"

service = ChromeService(executable_path=ChromeDriverManager().install())
options = ChromeOptions()
driver = webdriver.Chrome(options=options, service=service)
driver.get(url)

driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button').click()
# to make sure content is fully loaded we can use time.sleep() after navigating to each page
time.sleep(3)


# calculating how many times we need to scroll down to load next set of reviews
total_number_of_reviews = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/span[2]/span[1]/span').text.split(" ")[0]
total_number_of_reviews = int(total_number_of_reviews.replace(',','')) if ',' in total_number_of_reviews else int(total_number_of_reviews)
print(total_number_of_reviews)

# click on total_number_of_reviews
driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/span[2]/span[1]/span').click()
time.sleep(3)

# find scroll layout
scrollable_div = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]')

# # Scroll as many times as necessary to load all reviews
for i in range(0,(round(total_number_of_reviews/10 - 1))):
  driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scrollable_div)
  time.sleep(3)

# finding all find more buttons
readmores = driver.find_elements(By.XPATH, '//*[@class="w8nwRe kyuRq"]')
for readmore in readmores:
    readmore.click()

# parsing html and data extraction
response = BeautifulSoup(driver.page_source, 'html.parser')
driver.close()
reviews = response.find_all('div', class_='jftiEf fontBodyMedium')

print(len(reviews))



temp_dict = {
  'rating': [],
  'date': [],
  'text': []
}
for review in reviews:
  review_rating = review.find('span', class_='kvMYJc')["aria-label"]
  review_date = review.find('span',class_='rsqaWe').text
  review_text = review.find('span',class_='wiI7pd').text
  print(review_rating)
  print(review_date)
  print(review_text)
  temp_dict['rating'].append(review_rating)
  temp_dict['date'].append(review_date)
  temp_dict['text'].append(review_text)


dico = pd.DataFrame(temp_dict)
dico.to_csv('test-airedale-hospital.csv', encoding='utf-8')
# function to gather relevant data from the reviews
# def get_review_summary(result_set):
#     rev_dict = {'Review Rate': [],
#         'Review Time': [],
#         'Review Text' : []}
#     for result in result_set:
#         review_rate = result.find('span', class_='kvMYJc')["aria-label"]
#         review_time = result.find('span',class_='rsqaWe').text
#         review_text = result.find('span',class_='wiI7pd').text
#         print(review_text)
#         print(review_rate)
#         print(review_time)
#         # rev_dict['Review Rate'].append(review_rate)
#         # rev_dict['Review Time'].append(review_time)
#         # rev_dict['Review Text'].append(review_text)
#     # return(pd.DataFrame(rev_dict))
#     return "jame"

# dico = get_review_summary(reviews)
# # print(dico)

# saving dictionary into a csv file
# dico.to_csv('test.csv')

# time taken 
# print("time taken: ",time.time()-start)