Role = input("What role are you? ")
Question = input("What is the term? ")
Answer = input("What is the defintion? ")


import json

class Flashcard:
    def __init__(self,words,definition):
        self.words = words
        self.definition = definition
    def to_dict(self):
        return {"make": self.words, "model": self.definition}


    with open("FlashCards.json", "w") as file:
        json.dump(flashcards_data, file, indent=4)


