def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def count_words(book_content):
    word_count = 0
    words = book_content.split()
    for word in words:
        word_count += 1
    print(word_count)

book_content = main()
count_words(book_content)