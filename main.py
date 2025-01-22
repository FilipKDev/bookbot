import string

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def count_words(book_content):
    word_count = 0
    words = book_content.split()
    for word in words:
        word_count += 1
    # print(word_count)

def count_characters(book_content):
    book_content_lowered = book_content.lower()
    character_count = {}
    characters = list(string.ascii_lowercase)
    characters.append(" ")

    for character in characters:
        character_count[character] = 0

    for book_character in book_content_lowered:
        for character in characters:
            if character == book_character:
                character_count[character] += 1
    print(character_count)
    return character_count

book_content = main()
count_words(book_content)
count_characters(book_content)