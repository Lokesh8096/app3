import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up OpenAI for Azure
openai.api_type = "azure"
openai.api_key = "fce9b34907b848a6902e5c37ddfc8512"
openai.api_base = "https://nw-tech-wu.openai.azure.com"
openai.api_version = "2023-06-01-preview"

def generate_response(prompt):
    try:
        # Prepare chat messages
        messages = [
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt},
        ]

        # Call Azure OpenAI API
        response = openai.ChatCompletion.create(
            engine="gpt-4o",  
            messages=messages,
        )

        # Return the assistant's response
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"An error occurred: {e}"

