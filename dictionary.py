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

# Defining constants
FILENAME = "dictionary.csv"


# Main Function
def main():

    # Load data
    words = file_load(FILENAME)

    # Print list of words
    print(words)

    print("hello!")

    # Save dictionary
    file_save(words, FILENAME)


# Function that register a new key-value pair
# def key_register():


# Function that searches a key by character
# def key_search_by_character():


# Function that searches a key by syllable
# def key_search_by_syllable():


# Function that prints all keys on screen
# def key_show_all():


# Function that updates the key of a key-value pair
# def key_update_key():


# Function that updates the value of a key-value pair
# def key_update_value():


# Function that deletes a key-value pair
# def key_delete():


# Function that loads the contents of a csv file into a list
def file_load(path):

    # Generate an empty list
    data = list()

    # With the csv file open (read-mode):
    with open(path, 'r') as file:

        # Get a dict reader to the file
        reader = csv.DictReader(file)

        # For each word-meaning pair in the file...
        for row in reader:

            # ...append pair to list
            data.append({'word': row['word'], 'meaning': row['meaning']})

    # Return generated list
    return data


# Function that exports the contents of a list to a csv file
def file_save(list, path):

    # With csv file open (write-mode)
    with open(path, 'w') as file:

        # Get a dict writer to the file
        writer = csv.DictWriter(file, fieldnames=['word', 'meaning'])

        # For each word-meaning pair in the list...
        for row in list:

            # ...copy pair to csv file
            writer.writerow({'word': row['word'], 'meaning': row['meaning']})


# Call Main Function
if __name__ == "__main__":
    main()