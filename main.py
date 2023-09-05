import csv
import random

# Get the user to pick the set
set_name = input('What set would you like to study? ')

# Define the path based on the set name
set_path = './' + set_name + '/'

# Define the csv file path
csv_file = set_path + set_name + '.csv'

# Initialize a dictionary to store flashcards
flashcards = {}

# Load flashcards from the CSV file
try:
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 2:
                word = row[0].strip()
                definitions = [definition.strip() for definition in row[1:]]
                flashcards[word] = definitions
except FileNotFoundError:
    print('File not found :(')

# Initialize a list to store the flashcards for spaced repetition
flashcard_queue = list(flashcards.keys())

# Main flashcard loop
while flashcard_queue:
    # Randomly select a flashcard
    random_flashcard = random.choice(flashcard_queue)
    correct_definitions = flashcards[random_flashcard]

    # Show the flashcard
    print(f"Word: {random_flashcard}")
    user_answer = input('Definition: ')

    # Check the user's answer
    if user_answer.strip() in correct_definitions:
        print("Correct!\n")
        flashcard_queue.remove(random_flashcard)
    else:
        print(f"Wrong; the correct answer(s) are: {', '.join(correct_definitions)}\n")

print("You have completed all the flashcards!")
