# 5. Dicionário eletrônico (Aurélio) - Requisitos mínimos:
#   - [FUNÇÃO] Cadastrar palavras e significados novos;
#   - [FUNÇÃO] Implementar uma estratégia de pesquisa de palavras por letra e sílabas;
#   - [FUNÇÃO] Implementar uma estratégia de exibição das palavras cadastradas;
#   - [FUNÇÃO] Implementar uma estratégia de atualização das palavras e significados cadastrados;
#   - Criar mensagens de erro para controlar possíveis entradas inconsistentes do jogador;
#   - [FUNÇÃO] Implementar uma estratégia de exclusão das palavras cadastradas; e
#   - [FUNÇÃO] Bônus: Criar uma estratégia para salvar os dados da agenda em um arquivo.


# Loading libraries
import sys                      # ...for error messages
import csv                      # ...for csv file-handling
from tabulate import tabulate   # ...for table printing

# Defining constants
FILENAME = "dictionary.csv"


# Main Function
def main():


# Function that register a new key-value pair
def key_register():


# Function that searches a key by character
def key_search_by_character():


# Function that searches a key by syllable
def key_search_by_syllable():


# Function that prints all keys on screen
def key_show_all():


# Function that updates the key of a key-value pair
def key_update_key():


# Function that updates the value of a key-value pair
def key_update_value():


# Function that deletes a key-value pair
def key_delete():


# Function that loads the contents of a csv file into a list
def file_load(path):

    # Generate an empty list
    list = list()

    # With the csv file open:
    with open(path) as file:

        # Get a dict reader to the file
        reader = csv.DictReader(file)

        # For each word-meaning pair in the file...
        for row in reader:

            # ...append pair to the list
            list.append({'word': row['word'], 'meaning': row['meaning']})

    # Return generated list
    return list


# Function that exports the contents of a list to a csv file
def file_save(list, path):

    with open(path, 'w') as file:

        writer = csv.DictWriter(file, fieldnames=['word', 'meaning'])

        for row in list:

            writer.writerow




name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})



# Call Main Function
if __name__ == "__main__":
    main()