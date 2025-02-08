from openai import OpenAI

api_key = "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"


system_prompt = '''You are a person from 2025, i need you to make cards 
that are going to be used to play the taboo game. How it works is there
is one word that the player is given and four words that are similar or 
would help the player get the main word'''
user_prompt = "Give me a random word and four synonyms"

api = OpenAI(api_key=api_key)


def main():
    completion = api.chat.completions.create(
        model="gpt-4o-mini",
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