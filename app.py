from flask import Flask, jsonify, request
import random
import TabooAPI_withAI

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask API is running!"

# Define the system prompt and logic for generating taboo cards
def generate_taboo_cards():
    # Random generation logic (simplified here)
    words = [
        TabooAPI_withAI.printFullTaboo(),
        TabooAPI_withAI.printFullTaboo(),
        TabooAPI_withAI.printFullTaboo()
    ]
    # Select a random word set
    main_word, taboo_words = random.choice(words)
    return {"main_word": main_word, "taboo_words": taboo_words}

@app.route('/generate-taboo', methods=['GET'])
def generate():
    taboo_cards = generate_taboo_cards()
    return jsonify(taboo_cards)  # Send back the taboo card as a JSON response

if __name__ == "__main__":
    app.run(debug=True)