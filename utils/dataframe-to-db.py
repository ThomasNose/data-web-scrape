from sqlalchemy import create_engine
import pandas as pd
import os, shutil
from datetime import datetime
import time
from dataframe import create_parquet

path = '/home/thomas/youtube-data/parquet/'

def postgresload(path):
    """This function inputs a parent directory for all parquet files,
    creates a csv variant in a separate folder, and loads all parquet/csv
    data in one go to the postgresql database."""

    # List of all date folders
    files = os.listdir(path)

    # Loop for listing every parquet file
    for date in files:
        path_parquet = os.listdir(path+date)

        # Final loop will add each file to a dataframe
        for parquet in path_parquet:

            # file path for parquet files and reading them to dataframe
            file_path = path + date + '/' + parquet
            data = pd.read_parquet(file_path)

            # Path to where all csv files will be stored /youtube_data/csv/
            path_csv   = (path+date).replace('parquet','csv')

            # If path for csv doesn't exist for the day, this creates it
            PathExist = os.path.exists(path_csv)
            if not PathExist:
                os.makedirs(path_csv)

            # csv file path is identical to parquet except for change from "parquet" to "csv"
            csv_file = file_path.replace('parquet','csv')
            # writing data to csv file
            data.to_csv(csv_file, index = False)

            # Reading csv files, adding load timestamp (from csv to postgresql database)
            # and aggregating all other files into a single data from (from df1 to df)
            df1            = pd.read_csv(csv_file)
            df1['load_ts'] = (datetime.now())
            #print(df1)
            try:
                df = pd.concat([df,df1])
                print("appended")
            except:
                df = df1

    # Engine opens a connection to local postgresql database so we can write pandas df to table
    engine = create_engine('postgresql://guest:guest@localhost:5432/youtube') # postgresql://user:pass@localhost:5432/database
    df.to_sql('dim_video', engine, if_exists='replace', index = False)

    return(path_csv)


# Initiates the data collection and parquet file creation
# comment out if you don't want more data being collected
create_parquet()

# sleep for good measure
time.sleep(5)

# makes df None to avoid any variable overlap
df = None

# loads data into sql
postgresload(path)

# finally deletes the csv folder (we want the csv only for loading purposes and the parquet for storing)
shutil.rmtree(path.replace('parquet','csv'))