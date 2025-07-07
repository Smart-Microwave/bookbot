#returns the total number of words
def get_num_words(book):
    counter = 0
    book_words = book.split()

    for word in book_words:
        counter += 1

    return f"Found {counter} total words"


#returns a dict of the count of each character 
def get_num_characters(book):
    counted_characters = {}
    text = book.lower()

    for char in text:
        if char in counted_characters:
            counted_characters[char] += 1

        else:
            counted_characters[char] = 1

    return counted_characters


#takes in a dictionary of counted characters, and makes a list of dictionaries with keys?
def key_value(items):
    list_of_characters = []

    for char in items:
        char_dict = {"char": char, "num": items[char]}
        list_of_characters.append(char_dict)


    def sort_on(item):
        return item["num"]

    list_of_characters.sort(reverse=True, key=sort_on)
    return list_of_characters
