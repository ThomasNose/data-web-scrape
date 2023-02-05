import pandas as pd
from youtube import video, scrape_vids

homepage = 'https://www.youtube.com'
video_list, url_list = scrape_vids(homepage)
video_views, video_title,video_publish_date,youtube_channel,video_url,video_tags = video(url_list)


print(len(youtube_channel),len(video_title),len(video_tags))
print(youtube_channel[2],video_title[2],video_tags[2])


# pandas dataframe currenctly doesn't work :( currently 01:32 too tired
def dataframe(*data,**args):

    data_list = []
    [data_list.append(data) for data in data]

    arg_list = []
    [arg_list.append(arg) for arg in args]

    df = pd.DataFrame(columns = arg_list, dtype = str)
    print(df.columns)
    for i in range(len(data)):
        print("appending")
        df.loc[i] = data_list[i]

    return(df)


columns = ['video_views', 'video_title','video_publish_date',\
               'youtube_channel','video_url','video_tags']

df = dataframe(video(url_list),columns)
print(df)