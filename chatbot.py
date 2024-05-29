import random
import spacy
import nltk
from nltk.tokenize import word_tokenize

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# Sample predefined responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm fine, thank you.", "Doing well, how about you?", "I'm great!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
}

# Preprocess the responses to lower case
responses = {key.lower(): value for key, value in responses.items()}

def get_response_with_entities(user_input):
    # Convert user input to lower case
    user_input = user_input.lower()
    
    # Tokenize user input
    user_tokens = word_tokenize(user_input)
    
    # Find a matching response
    for key in responses.keys():
        if key in user_input:
            return random.choice(responses[key])
    
    # Use spaCy for entity recognition
    doc = nlp(user_input)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    if entities:
        return f"I see you mentioned {entities[0][0]} which is a {entities[0][1]}."
    
    # Default response if no match is found
    return "I'm not sure how to respond to that."

# Chat function to interact with the user
def chat():
    print("Chatbot: Hi! How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'exit', 'quit']:
            print("Chatbot: Goodbye!")
            break
        response = get_response_with_entities(user_input)
        print(f"Chatbot: {response}")

# Start the chat
chat()
