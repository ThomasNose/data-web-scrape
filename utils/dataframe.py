import pandas as pd
from youtube import video, scrape_vids

from datetime import datetime
import os

homepage = 'https://www.youtube.com'
video_list, url_list = scrape_vids(homepage)
stamp = datetime.now()

# pandas dataframe currenctly doesn't work :( currently 01:32 too tired
def dataframe(data):

    video_views, \
    video_title, \
    video_publish_date, \
    youtube_channel, \
    video_url, \
    video_tags          = data

    columns = ['video_views', 'video_title','video_publish_date',\
                'youtube_channel','video_url','video_tags']

    df = {'youtube_channel':[], 'video_title':[], 'video_views':[],'video_url':[], \
          'video_publish_date':[],'video_tags':[],'process_date':[]}

    for i in range(len(video_title)):
        df["video_views"].append(video_views[i])
        df["video_title"].append(video_title[i])
        df["video_publish_date"].append(video_publish_date[i])
        df["youtube_channel"].append(youtube_channel[i])
        df["video_url"].append(video_url[i])
        df["video_tags"].append(video_tags[i])
        df["process_date"].append(str(stamp)[0:19])

    df1 = pd.DataFrame(df)

    return(df1)



def create_parquet():

    df = None
    df = dataframe(video(url_list))

    path = '/home/thomas/youtube-data/parquet/process_date[{0}]/'.format(str(stamp)[0:10])
    PathExist = os.path.exists(path)
    if not PathExist and df.empty == False:
        os.makedirs(path)

    if df.empty == False:
        df.to_parquet(path=path+'process_time[{0}].parquet'.format(str(stamp)[11:19].replace(':','-')))