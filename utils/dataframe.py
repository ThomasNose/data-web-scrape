import pandas as pd
from youtube import video, scrape_vids

homepage = 'https://www.youtube.com'
video_list, url_list = scrape_vids(homepage)
#video_views, video_title,video_publish_date,youtube_channel,video_url,video_tags = video(url_list)


#print(len(youtube_channel),len(video_title),len(video_tags))
#print(youtube_channel[2],video_title[2],video_tags[2])


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

    df = {'video_views':[], 'video_title':[],'video_publish_date':[],\
                'youtube_channel':[],'video_url':[],'video_tags':[]}

    for i in range(len(video_title)):
        df["video_views"].append(video_views[i])
        df["video_title"].append(video_title[i])
        df["video_publish_date"].append(video_publish_date[i])
        df["youtube_channel"].append(youtube_channel[i])
        df["video_url"].append(video_url[i])
        df["video_tags"].append(video_tags[i])

    df1 = pd.DataFrame(df)

    return(df1)

df = dataframe(video(url_list))
print(df)