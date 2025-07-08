import sys
from stats import get_num_words, get_num_characters, key_value

#takes in the file path and returns the contents of that file
def get_book_text(path_to_file):
    with open(path_to_file) as file:
        file_contents = file.read()
    
        return file_contents


def print_report(path):
    book_text = get_book_text(path)
    word_count = get_num_words(book_text)
    char_count = key_value(get_num_characters(book_text))

    print(f"""============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
{word_count}
--------- Character Count -------""")    

    for dictionary in char_count:
        character = dictionary["char"]
        if character.isalpha():
            print(f"{character}: {dictionary["num"]}")



def main():
    if len(sys.argv) == 2:
        path = sys.argv[1]
        print_report(path)
    
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
if __name__ == "__main__":
    main()

