# load.py

import os
import pandas as pd
import sqlite3

DATA_DIR = "/opt/airflow/data" 

def load_to_sqlite():
    # Load the cleaned CSV
    df = pd.read_csv(os.path.join(DATA_DIR, "clean_data.csv"))

    # Create SQLite DB file (if doesn't exist)
    conn = sqlite3.connect(os.path.join(DATA_DIR, "youtube_trending.db"))

    # Write to a table named 'trending_videos'
    df.to_sql("trending_videos", conn, if_exists="replace", index=False)

    conn.close()
    print("✅ Data loaded into SQLite database (youtube_trending.db)")

if __name__ == "__main__":
    load_to_sqlite()
