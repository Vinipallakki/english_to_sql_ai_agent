from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_experimental.sql import SQLDatabaseChain
from config.settings import MODEL_NAME, GEMINI_API_KEY  # make sure you store your key in settings
from .bq_connection import get_bq_connection

def get_sql_agent():
    # Use API key instead of ADC/OAuth
    llm = ChatGoogleGenerativeAI(
        model=MODEL_NAME,
        api_key=GEMINI_API_KEY
    )
    db = get_bq_connection()
    return SQLDatabaseChain.from_llm(llm, db, verbose=True)
