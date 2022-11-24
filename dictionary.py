# 5. Dicionário eletrônico (Aurélio) - Requisitos mínimos:
#   - (OK) Cadastrar palavras e significados novos;
#   - (TO DO) Implementar uma estratégia de pesquisa de palavras por letra e sílabas;
#   - (OK) Implementar uma estratégia de exibição das palavras cadastradas;
#   - (OK) Implementar uma estratégia de atualização das palavras e significados cadastrados;
#   - (TO DO) Criar mensagens de erro para controlar possíveis entradas inconsistentes do usuário;
#   - (OK) Implementar uma estratégia de exclusão das palavras cadastradas; e
#   - (OK) Bônus: Criar uma estratégia para salvar os dados da agenda em um arquivo.

# Import libraries/functions
from os import system, name             # ...for screen clearing
from sys import exit                    # ...for program exiting
from csv import DictReader, DictWriter  # ...for CSV file-handling
from difflib import get_close_matches   # ...for word searching

# Define constants
PATH_TO_CSV_FILE = "dictionary.csv"  # Path to dictionary


# Main Function
def main():

    # Load dictionary from CSV file
    dictionary = file_load(path=PATH_TO_CSV_FILE)

    # Create infinite loop
    while True:

        # Clear the screen
        screen_clear()

        # Print program menu
        print_menu()

        # Prompt user for option
        try:
            option = int(input('Select an option: '))
        except ValueError:
            option = 0

        # While invalid option:
        while option not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:

            # Re-prompt user for option
            try:
                option = int(input('Invalid option. Select an option:'))
            except ValueError:
                option = 0

        # Blank line
        print()

        # If "List words" selected:
        if option == 1:

            # Call list keys function
            dictionary_keys_list_all(dictionary=dictionary)

        # Else, if "Search word by letter" selected:
        elif option == 2:

            # Call search by letter function
            dictionary_keys_search_by_character(dictionary=dictionary)

        # Else, if "Search word by syllable" selected:
        elif option == 3:

            # Call search by syllable function
            dictionary_keys_search_by_syllable(dictionary=dictionary)

        # Else, if "Search whole word" selected:
        elif option == 4:

            # Call search whole word function
            dictionary_keys_search_whole_word(dictionary=dictionary)

        # Else, if "Add new word-meaning" selected:
        elif option == 5:

            # Call add key function
            dictionary_key_add(dictionary=dictionary)

        # Else, if "Update word" selected:
        elif option == 6:

            # Call update key function
            dictionary_key_update(dictionary=dictionary)

        # Else, if "Update meaning" selected:
        elif option == 7:

            # Call update value function
            dictionary_value_update(dictionary=dictionary)

        # Else, if "Delete word" selected:
        elif option == 8:

            # Call delete key function
            dictionary_key_remove(dictionary=dictionary)

        # Else ("Exit program" selected):
        else:

            # Save dictionary to csv file
            file_save(dictionary, PATH_TO_CSV_FILE)

            # Exit program
            exit('Exiting program...')

        # Halt program until user presses any key
        input('\nOperation complete! Press any key to continue...')


def print_menu() -> None:
    ''' Prints menu on screen. 
        Returns nothing. '''

    print("""
        ===============================
        | ----  DICTIONARY MENU  ---- |
        ===============================
        1. List all words
        2. Search word (by letter)
        3. Search word (by syllable)
        4. Search whole word
        
        5. Add new word (and meaning)
        6. Update a word
        7. Update a meaning
        9. Delete a word (and meaning)
        
        9. Exit program
        ===============================
        """)


def dictionary_keys_list_all(dictionary: dict) -> None:
    ''' Prints all keys of input dict on screen. 
        Returns nothing. '''

    # Print a header
    print('WORDS IN DICTIONARY:')

    # For each key in dictionary:
    for key in sorted(dictionary):
        n_key = str(key).capitalize()
        # Print key
        print(f'- {n_key}')


def dictionary_keys_search_by_character(dictionary: dict) -> None:
    ''' Searches a key by character in input dict. 
        Returns nothing? '''

    # Print a header
    print("SEARCH WORD BY LETTER: \n")

    letter = input("Input letter to search: ").strip().lower()

    while len(letter) > 1:

        letter = input('Enter a single character to search: ')

    words = [key for key, value in dictionary.items() if letter in key]
    words.sort()
    n_words = [word.capitalize() for word in words]
    new_line = "\n"
    if len(words) != 0:
        print(f"\nThese are the results:{new_line}{new_line.join(n_words)}")
    else:
        print("Sorry we couldn't find any word that matched your search.")

    # ans = input(
    #     "\nWould you like to check one of these words? (Y/N) ").strip().lower()
    # while ans not in ["y", "n"]:

    #     ans = input(
    #         'Invalid option. Would you like to check one of these words? (Y/N) ')

    # if ans == "y":
    #     print('\nChoose one of the words:\n')
    #     for a, b in enumerate(words, 1):
    #         print(f'{a} {b}')

    #     option = int(input())


def dictionary_keys_search_by_syllable(dictionary: dict) -> None:
    ''' Searches a key by syllable in input dict. 
        Returns nothing? '''

    # Print a header
    print('SEARCH WORD BY SYLLABLE:\n')

    letter = input("Input syllable to search: ").strip().lower()
    words = [key for key, value in dictionary.items() if letter in key]
    words.sort()
    n_words = [word.capitalize() for word in words]
    new_line = "\n"
    if len(words) != 0:
        print(f"\nThese are the results:{new_line}{new_line.join(n_words)}")
    else:
        print("Sorry we couldn't find any word that matched your search.")


def dictionary_keys_search_whole_word(dictionary: dict) -> None:
    print('SEARCH WHOLE WORD:')

    # Prompt user for search key
    key = input("Input word to search: ").strip().lower()
    n_key = str(key.capitalize())
    # If word is already added to dict, just print
    if key in dictionary.keys():
        # Fazer o print com word -> meaning melhor
        print(n_key, ":", dictionary[key])

    elif len(get_close_matches(key, dictionary.keys())) > 0:
        ans = input("Did you mean % s instead? Enter Y if yes, or N if no: " %
                    get_close_matches(key, dictionary.keys())[0].capitalize())
        ans = ans.lower()
        if ans == "y":
            print(get_close_matches(key, dictionary.keys())[0].capitalize(
            ), ":", dictionary[get_close_matches(key, dictionary.keys())[0]])
        elif ans == "n":
            print(
                "The word doesn't exist in our database. Please check again or add the word to the database.")
        else:
            print("We didn't understand your entry.")
    else:
        print("The word doesn't exist in our database. Please check again or add the word to the database.")


def dictionary_key_add(dictionary: dict) -> dict:
    ''' Adds a new key:value pair to input dict. 
        Returns updated dict. '''

    # Prompt user for new key
    key = input("Input new word: ").strip().lower()

    # Prompt user for new key's value
    value = input("Input new word's meaning: ").strip().capitalize()

    # Add new key:value pair to dictionary
    dictionary[key] = value

    # Return dictionary
    return dictionary


def dictionary_key_update(dictionary: dict) -> dict:
    ''' Copies value from old key to new key in input dict.
        Deletes old key.
        Returns updated dict.'''

    # Prompt user for key to be replaced
    key_old = input('Which word to replace? ')

    # While key not in dictionary:
    while key_old not in dictionary.keys():

        # Re-prompt user for key
        key_old = input(f'Word "{key_old}" is not in dictionary. '
                        'Which word to replace? ')

    # Prompt user for new key
    key_new = input('Input new word: ').strip().lower()

    # Create new key with old key's value
    dictionary[key_new] = dictionary[key_old]

    # Delete old key
    del dictionary[key_old]

    # Return dictionary
    return dict


def dictionary_key_remove(dictionary: dict) -> dict:
    ''' Deletes a key-value pair from input dict.
        Returns updated dict. '''

    # Print a header
    print('DELETE A WORD:')

    # Prompt user for key to be deleted
    key = input('Which word to delete? ').strip().lower()

    # While key not in dict:
    while key not in dictionary:

        # Re-prompt user for key
        key = input(f'Word "{key}" is not in dictionary. '
                    'Which word to delete? ')

    # Remove key (and value) from dictionary
    del dictionary[key]

    # Return dictionary
    return dictionary


def dictionary_value_update(dictionary: dict) -> dict:
    ''' Replaces the value of a key in input dict.
        Returns updated dict. '''

    # Print a header
    print('UPDATE A MEANING:')

    # Prompt user for key whose value will be updated
    key = input('Update the meaning of which word? ').strip().lower()

    # While key not in dict:
    while key not in dictionary:

        # Re-prompt user for key
        key = input(f'Word "{key}" is not in dictionary. '
                    'Update the meaning of which word? ')

    # Prompt user for new meaning
    meaning = input(f'Input new meaning for "{key}": ')

    # Update value for key in dictionary
    dictionary[key] = meaning

    # Return dictionary
    return dictionary


def file_load(path: str) -> dict:
    ''' Loads the contents of a CSV file to a dict.
        Returns created dict'''

    # Create an empty dict
    dictionary = {}

    # Open CSV file in read-mode:
    with open(path, 'r') as file:

        # Get a dict reader to the file
        reader = DictReader(file)

        # For each word-meaning pair in the file...
        for row in reader:

            # Add word-meaning as key:value in dict
            dictionary[row['word']] = row['meaning']

    # Return dict
    return dictionary


def file_save(dictionary: dict, path: str) -> None:
    ''' Creates a CSV file and copies content of input dict to it. 
        Returns nothing. '''

    # Create (or re-create) CSV file in write-mode
    with open(path, 'w') as file:

        # Get a dict writer to the file
        writer = DictWriter(file, fieldnames=['word', 'meaning'])

        # Write fieldnames as headers in csv file
        writer.writeheader()

        # For each key in dictionary:
        for key in dictionary:

            # ...copy key:value pair from dictionary to csv file
            writer.writerow({'word': key, 'meaning': dictionary[key]})


def screen_clear() -> None:
    ''' Clears the screen.
        Returns nothing. '''

    # If OS is Windows:
    if name == 'nt':

        # Clear screen
        _ = system('cls')

    # Else, if OS is Linux or Mac:
    elif name == 'posix':

        # Clear screen
        _ = system('clear')

    # Else (unidentified OS):
    else:

        # Print "Can't identify OS" error message
        print('\nERROR: Could not identify OS. \
            Screen clearing disabled.', end='\n\n')


# Call main function
if __name__ == "__main__":
    main()
