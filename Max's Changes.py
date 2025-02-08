from openai import OpenAI

base_url = "https://api.aimlapi.com/v1"

# Insert your AIML API Key in the quotation marks instead of my_key:
api_key = "sk-ijklmnopabcd5678ijklmnopabcd5678ijklmnop" 

system_prompt = "You are a taboo AI"
user_prompt = "Give me a five random words and nothing else, seperated by spaces, no punctuation"

api = OpenAI(api_key=api_key, base_url=base_url)

#returns an array of words, the first being the title word, the rest being taboo words.
def getWords():
    completion = api.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.7,
        max_tokens=256,
    )

    response = completion.choices[0].message.content
    result = response.split(',')




    #response = ["Cat", "Mouse", "Pet", "Dog", "Whisker"]

    #print("User:", user_prompt)
    print(response)


getWords()

