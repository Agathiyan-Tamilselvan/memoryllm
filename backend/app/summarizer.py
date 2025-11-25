import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_memory(text: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Summarize the following conversation concisely."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content