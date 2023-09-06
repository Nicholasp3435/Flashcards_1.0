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
            definitions = [definition.strip() for definition in row[1:]]
            
            card = Card(term, definitions)
            flashcards.append(card)
    
    return flashcards

# draws a card at the specified index
def draw_card(card_stack, index=0):
    if (0 <= index and index < len(card_stack)):
        card = card_stack.pop(index)
        return card

# asks the user for the definition of a card
def ask_card(card):
    print(f"Term: {card.term}")
    answer = input("Definition: ")
    return (answer in card.definitions)

# adds a card to the specified index
def add_card(card_stack, card,  index):
    card_stack.insert(index, card)

# studies a card stack
def study_cards(study_stack):
    random.shuffle(study_stack)
    while(len(study_stack) > 0):
        visible_card = draw_card(study_stack)
        if not(ask_card(visible_card)):
            add_card(study_stack, visible_card, random.randint(0, len(study_stack)))
            print(f"Wrong; correct answer(s) are: {visible_card.definitions}\n")
        else:
            print("Correct :3\n")
    
# debug stacks
def print_stack(card_stack):
    for i in range(len(card_stack)):
        print(card_stack[i])

flashcard_stack = load_flashcards(sample_csv)
study_cards(flashcard_stack)
