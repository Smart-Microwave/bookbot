#returns the total number of words
def get_num_words(book):
    word_count = len(book.split())
    return f"Found {word_count} total words"


#returns the count of each character as a dictionary
def get_num_characters(book):
    counted_characters = {}
    text = book.lower()

    for char in text:
        if char in counted_characters:
            counted_characters[char] += 1

        else:
            counted_characters[char] = 1

    return counted_characters


#takes in a dictionary of counted characters, and makes a list of dictionaries with key value pairs
def key_value(items):
    list_of_characters = []

    for char in items:
        char_dict = {"char": char, "num": items[char]}
        list_of_characters.append(char_dict)


    def sort_on(item):
        return item["num"]

    list_of_characters.sort(reverse=True, key=sort_on)
    return list_of_characters
