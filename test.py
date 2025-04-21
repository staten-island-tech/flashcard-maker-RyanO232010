import json


class FlashCardApp:
    def __init__(self, file_name='FlashCards.json'):
        self.file_name = file_name
        self.flashcards = {}
        self.flashcards.update(self.load_flashcards())

    # Function to load flashcards (without os)
    def load_flashcards(self):
        try:
            with open(self.file_name, 'r') as file:
                content = file.read().strip()
                if not content:
                    return {}  # File is empty, start with no flashcards
                return json.loads(content)
        except FileNotFoundError:
            return {}  # File doesn’t exist yet, no problem!
        except json.JSONDecodeError:
            print("Oops! The flashcards file is broken. Starting with an empty set.")
            return {}


    # Function to save flashcards to the file
    def save_flashcards(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.flashcards, file, indent=4)

    # Teacher Mode
    def teacher_mode(self):
        while True:
            word = input("Enter the word/phrase (or type 'exit' to stop): ")
            if word.lower() == 'exit':
                break
            answer = input(f"Enter the answer for '{word}': ")
            self.flashcards[word] = answer
            self.save_flashcards()
            print(f"Flashcard for '{word}' added!")
        print("Teacher Mode exited.")

    # Student Mode
    def student_mode(self):
        if not self.flashcards:
            print("No flashcards available. Please add some in Teacher Mode first.")
            return

        correct_answers = 0
        streak = 0
        max_streak = 0
        total_questions = len(self.flashcards)

        questions = list(self.flashcards.keys())

        for word in questions:
            answer = input(f"What is the answer to '{word}': ")
            if answer.lower() == self.flashcards[word].lower():
                correct_answers += 1
                streak += 1
                max_streak = max(max_streak, streak)
                print("Correct!")
            else:
                streak = 0
                print(f"Incorrect! The correct answer is: {self.flashcards[word]}")

        print("\nYour score:")
        print(f"Correct Answers: {correct_answers}/{total_questions}")
        print(f"Max Streak: {max_streak}")
        print("Student Mode exited.")

    # Main function to navigate between Teacher and Student modes
    def run(self):
        while True:
            mode = input("Choose Mode: (Teacher/Student/Exit): ").lower()

            if mode == 'teacher':
                self.teacher_mode()
            elif mode == 'student':
                self.student_mode()
            elif mode == 'exit':
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please choose 'Teacher', 'Student', or 'Exit'.")

# Entry point for running the application
if __name__ == "__main__":
    app = FlashCardApp()
    app.run()