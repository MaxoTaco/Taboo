print("hello!") 
print("What's up maxiiii kiswa https://prod.liveshare.vsengsaas.visualstudio.com/join?7F96A7DAED1BB8E5F50184A62D00FB73A951")


from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message);
