# 📊 YouTube Trending Data Pipeline with Airflow, Docker & Python

This project builds an end-to-end **ETL data pipeline** that fetches real-time trending video data from the **YouTube Data API**, cleans the data, and loads it into a **SQLite database** using **Apache Airflow**. The entire workflow is containerized using **Docker** for portability and reproducibility.

---

## 🚀 Project Overview

### ✅ What It Does:
- 📥 **Extract:** Pulls trending video data via YouTube API (for India region)
- 🧹 **Transform:** Cleans and structures the raw JSON into a tabular CSV
- 🗃️ **Load:** Saves cleaned data into a SQLite database for querying
- 🛠️ **Orchestrates:** All steps automated using Apache Airflow DAGs
- 📦 **Runs in Docker:** Fully containerized for easy setup and deployment

---

## 🛠️ Tech Stack

| Tool            | Purpose                             |
|-----------------|-------------------------------------|
| Python          | ETL scripting                       |
| Pandas          | Data manipulation                   |
| SQLite          | Lightweight relational DB           |
| Apache Airflow  | Workflow orchestration              |
| YouTube Data API| Data source                         |
| Docker          | Containerized environment           |

---

## 📁 Folder Structure

<pre><code> docker/ ├── airflow/ │ ├── dags/ │ │ └── youtube_dag.py # Airflow DAG definition │ ├── scripts/ │ │ ├── extract.py # YouTube API data extractor │ │ ├── transform.py # Data cleaning script │ │ └── load.py # Load data into SQLite │ ├── data/ │ │ ├── raw_data.json # Raw YouTube API output │ │ ├── clean_data.csv # Cleaned CSV data │ │ └── youtube_trending.db # Final SQLite database │ └── airflow.cfg (optional) # Airflow config (ignored in .gitignore) │ ├── docker-compose.yml # Docker orchestration file ├── Dockerfile # Custom Airflow Docker image ├── README.md # Project documentation └── .gitignore # Prevents heavy/log files from uploading </code></pre>

## ⚙️ How to Run the Project

### 🔧 Prerequisites
- Docker & Docker Compose installed
- Valid YouTube Data API key (free from [Google Cloud Console](https://console.cloud.google.com/))

Insert your API key into extract.py:
API_KEY = "YOUR_API_KEY"

Start Airflow:
docker-compose up -d --build

Open Airflow UI:

Visit: http://localhost:8080

Login: admin / (password auto-generated in logs)

Trigger the DAG:

Turn on the DAG named youtube_trending_pipeline
Click ▶️ Trigger button

Check Outputs:

Visit docker/airflow/data/ to see:

raw_data.json
clean_data.csv
youtube_trending.db

