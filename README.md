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
1) sudo apt install python3-pip
2) pip install virtualenv
3) virtualenv .venv 
4) source .venv/bin/activate
4) pip install -r requirements.txt


**When complete, run dataframe.py**



**ISSUES**
>The initial scrape function sometimes stops looping despite being coded to run intil data is gathered (youtube might have a timeout/request limit)
>Unable to get the likes/dislikes of a youtube video easily 

