import nltk
import random
import re
import numpy as np

# Download NLTK resources (only need to run this once)
nltk.download('punkt')

# Sample responses
responses = {
    "greeting": ["Hello!", "Hi there!", "How can I help you today?", "Hey!"],
    "goodbye": ["Goodbye!", "See you later!", "Take care!", "Have a nice day!"],
    "thanks": ["You're welcome!", "No problem!", "Happy to help!", "Anytime!"],
    "default": ["I'm sorry, I didn't understand that.", "Could you rephrase that?", "I'm not sure how to respond to that."]
}

# Keywords for matching user input
keywords = {
    "greeting": ["hi", "hello", "hey", "howdy"],
    "goodbye": ["bye", "goodbye", "see you", "later"],
    "thanks": ["thank", "thanks", "thank you"]
}

def respond_to_user(input_text):
    input_text = input_text.lower()

    # Check for keywords in user input
    for key, words in keywords.items():
        for word in words:
            if re.search(r'\b' + re.escape(word) + r'\b', input_text):
                return random.choice(responses[key])
    
    return random.choice(responses["default"])

def chatbot():
    print("Welcome to the Chatbot! Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        
        response = respond_to_user(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()