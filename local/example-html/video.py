from bs4 import BeautifulSoup as bs
import requests

# This code reads a local .html file in search for values
with open('local/video.html','r') as local:

    content = local.read()
    # (content, 'lxml') is a parser to make the return "prettier"
    soup = bs(content, 'lxml')
    #print(soup.prettify())
    
    # Collecting video data once we have it loaded
    video_data = soup.find_all('span', class_='style-scope yt-formatted-string bold', limit=3)


    #for data in video_data:
    #    print("video views are " + str(data))

    print("video views are " + str(video_data[0].text))
    print("video was posted on " + str(video_data[2].text))