This code is being designed to collect data from youtube's homepage, as an anonymous user, as part of an ETL pipeline to
gain some insight into the trends, tags, views, titles, etc throughout the duration of the day.


**Current plan is**
1) python code scrapes data
2) put data into a pandas dataframe with ~30-60 minute time deltas (to allow for homepage update)
3) store data as parquet?
4) move data to postgresql server

This will hopefully be orchestrated by airflow (or other scheduling software) for automation of code



**INSTALLATION INSTRUCTIONS**

**Can be completed via the script "setup.sh"**
1) sudo apt install python3-pip
2) pip install virtualenv
3) virtualenv .venv 
4) pip install -r requirements.txt

5) when running code you must be in the virtual environment - source .venv/bin/activate
**To run the code you should run dataframe.py**



**ISSUES**
>The initial scrape function sometimes stops looping despite being coded to run intil data is gathered (youtube might have a timeout/request limit)
>Pandas dataframe currently not being created correctly - this is an issue with me not knowing pandas so well
>Unable to get the likes/dislikes of a youtube video easily 

