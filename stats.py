def get_word_count(book):
    words = book.split()
    return len(words)

def get_char_count(book):
    dict_count = {}
    for i in book:
        c = i.lower()
        if c in dict_count:
            dict_count[c] += 1
        else:
            dict_count[c] = 1
    return dict_count
