# DROP TABLES

songplay_table_drop = "drop table if exists songplays"
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists songs"
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE songplays
  (
     songplay_id SERIAL PRIMARY KEY,
     start_time  TIMESTAMP NOT NULL,
     user_id     INT NOT NULL,
     level       TEXT,
     song_id     TEXT,
     artist_id   TEXT,
     session_id  INT,
     location    TEXT,
     user_agent  TEXT
  ) 
""")

user_table_create = ("""
CREATE TABLE users
  (
     user_id    INT PRIMARY KEY,
     first_name TEXT,
     last_name  TEXT,
     gender     TEXT,
     level      TEXT
  ) 
""")

song_table_create = ("""
CREATE TABLE songs
  (
     song_id   TEXT PRIMARY KEY,
     title     TEXT NOT NULL,
     artist_id TEXT,
     year      INT,
     duration  FLOAT NOT NULL
  ) 
""")

artist_table_create = ("""
CREATE TABLE artists
  (
     artist_id TEXT PRIMARY KEY,
     NAME      TEXT NOT NULL,
     location  TEXT,
     latitude  FLOAT,
     longitude FLOAT
  ) 
""")

time_table_create = ("""
CREATE TABLE time
  (
     start_time TIMESTAMP PRIMARY KEY,
     hour       INT,
     day        INT,
     week       INT,
     month      INT,
     year       INT,
     weekday    VARCHAR
  ) 
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays
            (
                        start_time,
                        user_id,
                        level,
                        song_id,
                        artist_id,
                        session_id,
                        location,
                        user_agent
            )
            VALUES
            (
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
            )
ON conflict
            (
                        songplay_id
            )
            do nothing
""")

user_table_insert = ("""
INSERT INTO users
            (
                        user_id,
                        first_name,
                        last_name,
                        gender,
                        level
            )
            VALUES
            (
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
            )
ON conflict
            (
                        user_id
            )
            do UPDATE
set    users.level = excluded.level
""")

song_table_insert = ("""
INSERT INTO songs
            (
                        song_id,
                        title,
                        artist_id,
                        year,
                        duration
            )
            VALUES
            (
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
            )
ON conflict
            (
                        song_id
            )
            do nothing
""")

artist_table_insert = ("""
INSERT INTO artists
            (
                        artist_id,
                        NAME,
                        location,
                        latitude,
                        longitude
            )
            VALUES
            (
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
            )
ON conflict
            (
                        artist_id
            )
            do nothing
""")


time_table_insert = ("""
INSERT INTO time
            (
                        start_time,
                        hour,
                        day,
                        week,
                        month,
                        year,
                        weekday
            )
            VALUES
            (
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
            )
ON conflict
            (
                        start_time
            )
            do nothing
""")

# FIND SONGS

song_select = ("""
SELECT s.song_id,
       a.artist_id
FROM   songs AS s
       join artists AS a
         ON s.artist_id = a.artist_id
WHERE  s.title =% s
       AND a.name =% s
       AND s.duration =% s 
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]