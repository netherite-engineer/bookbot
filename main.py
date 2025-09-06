import sys
from stats import get_word_count, get_char_count, get_report

if len(sys.argv) < 2:
    sys.exit("Usage: python3 main.py <path_to_book>")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    #return print(get_book_text("books/frankenstein.txt"))
    book = get_book_text(sys.argv[1])
    word_count = str(get_word_count(book))
    char_count = get_char_count(book)

    # return print(str(get_word_count(book)) + " words found in the document"), print(get_char_count(book)), get_report("books/frankenstein.txt",word_count, char_count)
    return get_report(sys.argv[1],word_count, char_count)
main()