# importing the libraries
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import requests
from time import sleep


# creating function
def scrape_vids(homepage):
    """This function is intended for the collection of videos from
    the youtube homepage"""

    driver = webdriver.Firefox()

    driver.get(homepage)

    html = driver.page_source

    videos = None
    urls = None


    # (content, 'lxml') is a parser to make the return "prettier"
    soup = bs(html, 'lxml')
        
    # style-scope ytd-rich-grid-slim-media for youtube shorts
    videos = soup.find_all('div', id='meta', class_='style-scope ytd-rich-grid-media')
    urls = soup.find_all('h3', class_='style-scope ytd-rich-grid-media')

    # video titles
    video_list = []
    [video_list.append(str(data.a["title"])) for data in videos]

    # video urls
    url_list = []
    [url_list.append(homepage + str(vid_url.a['href'])) for vid_url in urls]

    
    # wait 2 seconds to avoid any trip ups (temp)
    sleep(2)
    driver.close()

    # if no data is collected then the function runs again.
    if len(video_list) != len(url_list) or len(video_list) == 0 or len(url_list) == 0:
        scrape_vids(homepage)

    return(video_list, url_list)

def video(url):
    """Function for collecting views, title, published_date, channel name,
    url, and tags over a list of youtube videos"""

    video_views         = []
    video_title         = []
    video_publish_date  = []
    youtube_channel     = []
    video_url           = []
    video_tags          = []

    for page in url:
        html = requests.get(page)

        # (content, 'lxml') is a parser to make the return "prettier"
        soup = bs(html.text, 'lxml')

        # Collecting video data once we have it loaded
        views          = soup.find("meta", itemprop="interactionCount")['content']
        title          = soup.find("meta", itemprop="name")['content']
        published_date = soup.find("meta", itemprop="datePublished")['content']
        channel        = soup.find("link", itemprop="name")['content']
        vid_url        = soup.find("meta", property="al:web:url")['content'].split('&')
        tags           = soup.find_all("meta", property="og:video:tag")

        tag_list = []
        [tag_list.append(tag["content"]) for tag in tags]

        video_views         .append(str(views))
        video_title         .append(str(title))
        video_publish_date  .append(str(published_date))
        youtube_channel     .append(str(channel))
        video_url           .append(str(vid_url[0]))
        video_tags          .append(str(tag_list))

    return(video_views,video_title,video_publish_date,youtube_channel,video_url,video_tags)