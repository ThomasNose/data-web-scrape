This code is being designed to collect data from youtube's homepage, as an anonymous user, as part of an ETL pipeline to
gain some insight into the trends, tags, views, titles, etc throughout the duration of the day.


**Current plan is**
1) python code scrapes data - **Done**
2) put data into a pandas dataframe with ~30-60 minute time deltas (to allow for homepage update) - **Done-ish**
3) store data as parquet? - **Done**
4) move data to postgresql server - **Done**

This will hopefully be orchestrated by airflow (or other scheduling software) for automation of code



**INSTALLATION INSTRUCTIONS**

**Can be completed via the script "setup.sh"**
1) run setup.sh
4) source .venv/bin/activate
4) pip install -r requirements.txt


**SCRIPTS AND WHAT THEY DO**
1) youtube.py collects html code from the youtube homepage as an anonymous user and organises it into obvious variable names

2) dataframe.py takes the data from youtube.py and puts it into a dictionary. The data is then stored as parquet files

3) dataframe-to-db.py uses the parquet files to create temporary csv files which are they used to concat into one large
   dataframe by looping over all the parquet files (for each run of web scraping). Once all files have been looped over
   and added to a single dataframe, the data is pushed to a local postgresql server database which has all values replaced
   to avoid duplication. (planning for time deltas)
   
4) These are the 3 main python scripts in utils/
    
   There are files in local/ which serve as basic code examples for scraping certain bits of data from certain parts of youtube
   e.g. channel.py is a youtube channel homepage, home.py is the youtube homepage etc. 
   
   channel, home, and video rely on .html files to function
   
5) test.py is literally meant for random testing


**ISSUES**
>The initial scrape function sometimes stops looping despite being coded to run intil data is gathered (youtube might have a timeout/request limit)
>Unable to get the likes/dislikes of a youtube video easily 

