import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_KEY")


def ask_gpt(message, prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": message}
            ],
            max_tokens=1000,
            temperature=0,
            # n=2,
        )
        answer = response["choices"][0]["message"]["content"]
        return answer
    except Exception as e:
        print(e)
