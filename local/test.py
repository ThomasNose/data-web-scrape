from selenium import webdriver
from bs4 import BeautifulSoup as bs

driver = webdriver.Firefox()

driver.get('http://www.youtube.com')

html = driver.page_source

soup = bs(html)
print(soup.prettify())