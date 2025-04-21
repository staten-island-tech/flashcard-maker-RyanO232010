Role = input("What role are you? ")
Question = input("What is the term? ")
Answer = input("What is the defintion? ")


import json

FLASHCARDS_FILE = 'FlashCards.json'

def load_flashcards():
    try:
        with open(FLASHCARDS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    
def save_flashcards(flashcards):
    with open(FLASHCARDS_FILE, 'w') as file:
        json.dump(flashcards, file, indent=4)


