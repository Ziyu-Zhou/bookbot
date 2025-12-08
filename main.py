from stats import get_num_words
from stats import get_book_text
from stats import get_num_character
from stats import sort_dictionary
import sys

def main():
    if len(sys.argv)< 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    content = get_book_text(book_path)
    # print(content)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    
    word_count = get_num_words(content)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    num_of_character = get_num_character(content)
    print("--------- Character Count -------")
    # print(num_of_character)


    # print("-----------list of dictionary----------")

    sorted_dict_list = sort_dictionary(num_of_character)
    for i in sorted_dict_list:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
