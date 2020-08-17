# glossaryFlashCards.py

# Version for 20D TMA03 Q2

"""
This flashcard program allows the user to ask for a glossary entry.
In response, the program can either randomly pick an entry from all glossary
entries or look for a specific one. If the user selects a random one, it shows the entry.
After the user presses return, the
program shows the definition of that particular entry.
If the user wants to look for a specific entry, they will be asked to type a word and if that word is found in the
glossary, its definition will be shown to them.
The user can repeatedly ask for a random or a specific entry and also
has the option to quit the program instead of seeing
another entry.
"""

from random import *

def show_flashcard():
    """ Show the user a random key and ask them
        to define it. Show the definition
        when the user presses return.    
    """
    random_key = choice(list(glossary))
    print('Define: ', random_key)
    input('Press return to see the definition')
    print(glossary[random_key])


# Set up the glossary

glossary = {'word1':'definition1',
            'word2':'definition2',
            'word3':'definition3'}

# Uncomment the next line and then complete the function for part aii.
"""
The function asks for the user input and looks for it in the glosarry.
If the input is found, its definition is printed.
If not, it will print a suitable
message. 
"""
def look_up_definition():
    user_input = input('Please enter your word: ')
    if user_input in glossary:
            print(glossary[user_input])
    else:
        print(f'{user_input} not found in glossary')



# The interactive loop

exit = False
while not exit:
    user_input = input('Enter s to show a flashcard, d to look up a definition and q to quit: ')
    if user_input == 'q':
        exit = True
    elif user_input == 's':
        show_flashcard()
    elif user_input == 'd':
        look_up_definition()
    else:
        print('You need to enter either q, d or s.')
                       
