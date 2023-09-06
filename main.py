import csv
import random
from card import Card



# default csv file
sample_csv = "./sample/sample.csv"


# loads a flashcard formatted csv file into an array or cards
def load_flashcards(csv_filename):
    flashcards = []
    
    with open(csv_filename, mode='r') as file:
        reader = csv.reader(file)
        
        for row in reader:
            term = row[0]
            definitions = row[1:]
            
            card = Card(term, definitions)
            flashcards.append(card)
    
    return flashcards

flashcard_stack = load_flashcards(sample_csv)


