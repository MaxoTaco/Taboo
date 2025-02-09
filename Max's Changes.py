from openai import OpenAI

api_key = "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"


number_of_taboo_words = 5
theme = "pirates of the carribean"


already_used_words = []

system_prompt = '''You should give different words related to: a late evening alone in the tub'''
user_prompt = '''Give me a list of five words. The first word is the main words.
 The next four are the four closest words to the main word. Respond with no other text.
   Seperate each word with a comma. Repeat this entire process five times, not repeating words. 
   Don't number the words. Don't repeat the same word multiple times. Don't use any of the following words: ''' 

api = OpenAI(api_key=api_key)


def prompt(system_prompt, user_prompt):
    completion = api.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.7,
        max_tokens=256,
        n=1
    )

    response = completion.choices[0].message.content

    return response



def processResponse(response):  
    return response.split(',')

def printFullTaboo():
    aiPrompt = (prompt('''Generate random words and synonyms with the theme of ''' + theme, 
           '''Give me a list of five words. The first word is the main words.
 The next ''' + str(number_of_taboo_words) + ''' are the ''' + str(number_of_taboo_words) + ''' closest words to the main word. Respond with no other text.
   Seperate each word with a comma.
   Don't number the words. Don't repeat the same word multiple times. Avoid words related to the following words:''' + str(already_used_words)))
    
    response = processResponse(aiPrompt)
    mainWord = response.pop(0)
    tabooWords = response
    print("The main word is: " + mainWord)
    print("Don't use any of the following words: " + ' '.join(tabooWords))

    already_used_words.append(mainWord)

if __name__ == "__main__":
    for i in range(50):
        printFullTaboo()

    print(already_used_words)


    
    
    