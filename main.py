import sys
from stats import get_num_words
from stats import get_num_characters
from stats import key_value


def input_check():
    if len(sys.argv) != 2:
        return False
    else:
        return True


def get_book_text(path_to_file):
    with open(path_to_file) as file:
        file_contents = file.read()
    
        return file_contents


def report(sorted_keyed_dictionary):

    print(f"""============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------""")    
    print(get_num_words(get_book_text(sys.argv[1])))
    print("--------- Character Count -------")

    for dictionary in sorted_keyed_dictionary:
        character = dictionary["char"]
        if character.isalpha():
            count = dictionary["num"]
            print(f"{character}: {count}")



def main():
    input_ok = input_check()
    if input_ok == True:
        report(key_value(get_num_characters(get_book_text(sys.argv[1]))))
    
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
main()

