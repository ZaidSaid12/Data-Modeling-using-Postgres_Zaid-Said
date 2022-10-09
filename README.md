# Sparkify
## Database Structure and Purpose
- In order to preserve the data for the company and support scalability and benefit from the data, we need to create a star schema which can hold the data for the played songs and the related dimensions
    - Fact Table: `songplays`
    - Dim Tables: `songs`, `artists`, `time`, `users`
- By getting the data of each user with the played songs, we can get the free users and provide sales for them or discounts to encourage them to be fully subscribed clients, provide better offers for existing subscribed clients, etc..

## Project Structure
Data Modeling with Postgres
- data
    - log files
        - ...
    - Data files
        - ...
- create_tables.py
- etl.ipynb
- etl.py
- README.md
- sql_queries.py
- test.ipynb

## How to run python scripts
1. first we need to run create_tables.py, in order to create the database and the tables using `python create_tables.py`
2. then we need to run the etl.py, in order to run the etls pipelines to populate the tables from the json files using `python etl.py`

## Explanation of the files
### sql_queries.py
- a file which contains sql queries for creating the tables and inserting statements to populate these tables, in addition to drop table statements
- the insert statements are templates for the inserts, when needed to insert into the table, we must pass the values in the `execute` function as shown in other files.
### create_tables.py
- this file uses `sql_queries.py` in order to create the tables and the database.
### etl.ipynb
- this notebook is a helper to know the exact steps to process 1 files in the songs files and logs files, then these steps will be used in the etl.py file, in order to process the whole directory
### etl.py
1. process_data
    Iterating dataset to apply process_song_file and process_log_file functions
2. process_song_file
    Process song dataset to insert record into songs and artists dimension table
3. process_log_file
    Process log file to insert record into time and users dimensio table and songplays fact table
### Database Schema
- since we have the log files of each song, which user listened to it, when, his account type, the author of the song.
- so we need a fact table to hold this data
- in addition to dimension tables to hold user data, author data, songs data, time data.
- Fact Table(s)
    - songplays
        - songplay_id SERIAL primary key, 
        - start_time timestamp NOT NULL, 
        - user_id int NOT NULL, 
        - level text, 
        - song_id text, 
        - artist_id text, 
        - session_id int, 
        - location text, 
        - user_agent text
- Dimension Table(s)
    - users
        - user_id int primary key, 
        - first_name text, 
        - last_name text, 
        - gender text, 
        - level text
    - artists
        - artist_id text primary key, 
        - name text NOT NULL, 
        - location text, 
        - latitude float, 
        - longitude float
    - songs
        - song_id text primary key, 
        - title text NOT NULL, 
        - artist_id text, 
        - year int, 
        - duration float NOT NULL
    - time
        - start_time TIMESTAMP PRIMARY KEY, 
        - hour INT, 
        - day INT, 
        - week INT, 
        - month INT, 
        - year INT, 
        - weekday VARCHAR
### ETL Pipeline
- Song Files
    - Extract data from the songs json files
    - get the related data for each dimension {songs, artists}
    - load the data into the tables
- Log Files
    - Extract data from the logs json files.
    - get the related data for users and time dimension tables {apply transformation on column ts}
    - load the data into dimension tables
    - perform suitable join to the the required data to be inserted into the fact table
    - load the data into songplays table
