import csv
import random
import os
from PIL import Image
from card import Card

# loads a flashcard formatted csv file into an array or cards
def load_flashcards(csv_directory):
    csv_filename = csv_directory + '/cards.csv'
    try:
        image_directory = csv_directory + '/images/'
    except:
        image_directory = None
        
    flashcards = []
    
    with open(csv_filename, mode='r') as file:
        reader = csv.reader(file)
        
        for row in reader:
            term = row[0]
            if (os.path.isfile(image_directory + term + '.png')):
                image = image_directory + term + '.png'
            else:
                image = None
                
            definitions = [definition.strip() for definition in row[1:]]
            
            card = Card(term, definitions, image)
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
    if not (card.image is None):
        im = Image.open(open(card.image, 'rb'))
        im.show()
        
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
    
# creates a card stack
def create_cards():
    card_stack = []
    while(True):
        term = input('Term: ')
        if (term.lower() == 'quit'):
            save = input('Would you like to save this set? (Y/n): ')
            if (save == 'Y'):
                name = input('What do you want to call this set? ')
                save_flashcards(card_stack, name)
            break
        definitions = input('Definition (use commas for multiple): ')
        definitions = definitions.split(',')
        new_card = Card(term, definitions)
        card_stack.append(new_card)
        print()
    

# saves a card array to a csv file
def save_flashcards(card_stack, name):
    directory_path = os.getcwd() + '/' + name
    cards_path = directory_path + '/cards.csv'
    exists = os.path.isfile(cards_path)
    if not(exists):
        os.mkdir(directory_path)
    else:
        overwrite = input('This file already exists, would you like to overwrite it? (Y/n): ')
        if (overwrite == "Y"):
            os.remove(cards_path)
        else:
            return
    with open(cards_path, 'w') as file:
        save_stack = []
        for card in card_stack:
            save_stack.insert(0,[card.term] + card.definitions)
        write = csv.writer(file)
        write.writerows(save_stack)
    
def start():
    print("Welcome to Nic's Flashcard App 1.0")
    purpose = input('Would you like to study or make some flashcards? (study/make): ')
    if (purpose == 'study'):
        study_set = input('What set would you like to study? ')
        cards = load_flashcards('./' + study_set)
        study_cards(cards)
    elif (purpose == 'make'):
        purpose = input('Would you like to edit a set or create a new one? (edit/new): ')
        if (purpose == 'new'):
            create_cards()
        elif (purpose == 'edit'):
            print('not yet implemented')
        

# debug stacks
def print_stack(card_stack):
    for i in range(len(card_stack)):
        print(card_stack[i])

start()
