import openai

openai.api_key ="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"


response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message['content'])
