import string

def main():
    book_content, book_file_path = open_file()
    book_word_count = count_words(book_content)
    book_character_dictionary = count_characters(book_content)
    book_character_sorted_list = sort_character_dictionary(book_character_dictionary)
    del book_character_sorted_list[0]
    generate_character_report(book_file_path, book_word_count, book_character_sorted_list)

def open_file():
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents, file_path

def count_words(content):
    word_count = 0
    words = content.split()
    for word in words:
        word_count += 1
    #print(f"This book has {word_count} words")
    return word_count

def count_characters(content):
    book_content_lowered = content.lower()
    character_count = {}
    characters = list(string.ascii_lowercase)
    characters.append(" ")

    for character in characters:
        character_count[character] = 0

    for book_character in book_content_lowered:
        for character in characters:
            if character == book_character:
                character_count[character] += 1
    #print(character_count)
    return character_count

def generate_character_report(file_path, word_count, character_sorted_list):
    print(f"--- Begin report of {file_path} ---")
    print(f"This document has {word_count} words")
    print("")
    for index in character_sorted_list:
        print(f"The {index["character"]} character was found {index["count"]} times")
    print("--- End report ---")

def sort_by_count(dict):
    return dict["count"]

def sort_character_dictionary(dictionary):
    character_list = []
    for characters in dictionary:
        list_dict = {}
        list_dict["character"] = f"'{characters}'"
        list_dict["count"] = dictionary[characters]
        character_list.append(list_dict)
    character_list.sort(reverse=True, key=sort_by_count)
    return character_list

main()