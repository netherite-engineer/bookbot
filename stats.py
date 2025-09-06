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

def sort_on(items):
    return items["num"]

def get_report(book_path, word_count, char_count):
    list = []
    for i in char_count:
        appears = char_count[i]
        if i.isalpha():
            list.append({"char": i, "num": appears})
    list.sort(reverse=True, key=sort_on)
    # report header
    header = "============ BOOKBOT ============\n"
    # statement 1
    pathstat = "Analyzing book found at " + book_path + "...\n"
    # word header
    wordhead = "----------- Word Count ----------\n"
    # statement 2
    wordstat = "Found " + word_count + " total words\n"
    # char header
    charhead = "--------- Character Count -------\n"
    print(header)
    print(pathstat)
    print(wordhead)
    print(wordstat)
    print(charhead)
    for i in list:
        body = i["char"] + ": " + str(i["num"]) + "\n"
        print(body)
    # end header
    endhead = "============= END ==============="
    print(endhead)
    return 