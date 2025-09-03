from stats import get_word_count

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    #return print(get_book_text("books/frankenstein.txt"))
    book = get_book_text("books/frankenstein.txt")
    return print(str(get_word_count(book)) + " words found in the document")

main()