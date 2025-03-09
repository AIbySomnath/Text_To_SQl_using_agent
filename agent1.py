import requests
from utils import generate_summary
import os
from dotenv import load_dotenv

load_dotenv()

AGENT2_URL = 'http://localhost:5000'  # URL where Agent 2 is running

def process_command(command):
    # Forward the command to Agent 2
    response = requests.post(
        f"{AGENT2_URL}/query",
        json={'command': command}
    )
    raw_data = response.json()['data']

    # Generate summary using OpenAI
    summary = generate_summary(raw_data)

    return raw_data, summary

# Example usage
if __name__ == "__main__":
    command = "Give me the account summary for January"
    raw_data, summary = process_command(command)
    print("Raw Data:", raw_data)
    print("Summary:", summary)
