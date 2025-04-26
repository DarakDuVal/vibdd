from dotenv import dotenv_values
from openai import OpenAI

secrets = dotenv_values(".env")

client = OpenAI(
    api_key=secrets['OPENAI_API_KEY']
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {"role": "user", "content": "write a haiku about ai"}
    ]
)

print(completion.choices[0].message)
