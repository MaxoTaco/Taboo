from openai import OpenAI

base_url = "https://api.aimlapi.com/v1"

# Insert your AIML API Key in the quotation marks instead of my_key:
api_key = "bca451b5d7304041ba4d09a32fe7247a" 

system_prompt = "You are a person from 2025, i need you to make cards that are going to be used to play the taboo game. How it works is there is one word that the player is given and "
user_prompt = "Give me a random word and four synonyms"

api = OpenAI(api_key=api_key, base_url=base_url)


def main():
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

    print("User:", user_prompt)
    print("AI:", response)


if __name__ == "__main__":
    main()