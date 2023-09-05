import csv
import random

# Get the user to pick the set
set = input('What set would you like to study? ')
    

# Defines the path based on the set name
set_path = './' + set + '/'

# Defines the csv file path
csv_file = set_path + set + '.csv'

# Initialize a dictionary to store flashcards
flashcards = {}

# Load flashcards from the CSV file
try:
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2:
                word, definition = row
                flashcards[word.strip()] = definition.strip()
except:
    print('File not found :(')

# Initialize a list to store the flashcards for spaced repetition
flashcard_queue = list(flashcards.keys())

# Main flashcard loop
while flashcard_queue:
    # Randomly select a flashcard
    random_flashcard = random.choice(flashcard_queue)
    correct_answer = flashcards[random_flashcard]

    # Show the flashcard
    print(f"Word: {random_flashcard}")
    user_answer = input('Definition: ')

    # Check the user's answer
    if user_answer.strip() == correct_answer:
        print("Correct!\n")
        flashcard_queue.remove(random_flashcard)
    else:
        print(f"Wrong; the correct answer is {correct_answer}\n")

print("You have completed all the flashcards!")
