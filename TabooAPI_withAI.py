
import os
import random
from openai import OpenAI

api_key = "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"

categories = [
    "Emotions", "Objects", "Actions", "Pop Culture", "Everyday Life"
]

system_prompt = '''You are an AI in the year 2025, generating **unique** Taboo cards.  
Each turn, create **completely new and diverse** Taboo cards.  

**Rules:**  
- Pick a **random** main word (NO fixed categories).  
- Generate **four Taboo words** that are closely related but **cannot be used** to describe the main word.  
- Ensure **no words repeat** within a session.  
- Repeat **10 times**, each with a **fresh new word set**.  
- Make the game **fun, engaging, and unpredictable**.  
'''
random_number = random.randint(1000, 9999)  # Adds variation to the prompt
user_prompt = f"Generate 10 completely unique Taboo cards. Session ID: {random_number}"


api = OpenAI(api_key=api_key)


def main():
    completion = api.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.9,
        max_tokens=256,
        n=1 
    )

    response = completion.choices[0].message.content

    print("User:", user_prompt)
    print("AI:", response)


if __name__ == "__main__":
    main()