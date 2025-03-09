import openai
import sqlite3
import pandas as pd
import os
from dotenv import load_dotenv
import spacy

# Load environment variables from .env file
load_dotenv()

# API keys and database credentials
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
DATABASE_PATH = os.getenv('DATABASE_PATH')

# Initialize OpenAI
openai.api_key = OPENAI_API_KEY

# Load NLP model
nlp = spacy.load('en_core_web_sm')

def generate_sql_query(question):
    # Advanced NLP to understand the question
    doc = nlp(question)
    table = "account_summary"  # Default table
    columns = "*"
    conditions = "1=1"  # Default condition (no filtering)

    # Example: Extracting month from the question
    for ent in doc.ents:
        if ent.label_ == "DATE":
            conditions = f"month = '{ent.text}'"

    query = f"SELECT {columns} FROM {table} WHERE {conditions}"
    return query

def execute_sql_query(query):
    # Execute the SQL query on the database
    conn = sqlite3.connect(DATABASE_PATH)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def generate_summary(data):
    # Generate summary using OpenAI
    summary_response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Summarize the following data: {data}",
        max_tokens=100
    )
    summary = summary_response.choices[0].text.strip()
    return summary