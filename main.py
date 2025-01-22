import string

def main():
    book_content = open_file()
    count_words(book_content)
    count_characters(book_content)

def open_file():
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def count_words(content):
    word_count = 0
    words = content.split()
    for word in words:
        word_count += 1
    print(f"This book has {word_count} words")
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
    print(character_count)
    return character_count


main()