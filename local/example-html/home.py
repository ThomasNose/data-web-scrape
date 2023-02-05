from bs4 import BeautifulSoup as bs
import requests

# This code reads a local .html file in search for values
with open('local/home.html','r') as local:

    content = local.read()
    # (content, 'lxml') is a parser to make the return "prettier"
    soup = bs(content, 'lxml')
    #print(soup.prettify())
    
    # style-scope ytd-rich-grid-slim-media for youtube shorts
    videos = soup.find_all('div', id='meta', class_='style-scope ytd-rich-grid-media')

    for data in videos:
        print("video title is " + str(data.a["title"]))
