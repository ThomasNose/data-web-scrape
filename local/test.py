import os

path = '/home/thomas/youtube-data/csv/'
files = os.listdir(path)

for date in files:
    csv_time = os.listdir(path+date)
    print(path+date)
    print(csv_time)