from langchain_community.utilities.sql_database import SQLDatabase
from config.settings import PROJECT_ID, DATASET_ID

def get_bq_connection():
    return SQLDatabase.from_uri(f"bigquery://{PROJECT_ID}/{DATASET_ID}")
