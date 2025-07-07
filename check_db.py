import sqlite3
import pandas as pd

conn = sqlite3.connect("C:\\Users\\vamsh\\OneDrive\\Desktop\\docker\\airflow\\data\\youtube_trending.db")
df = pd.read_sql("SELECT * FROM trending_videos LIMIT 5", conn)
print(df)
conn.close()
