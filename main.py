from stats import get_num_words
from stats import get_book_text
from stats import get_num_character

def main():
    content = get_book_text("books/frankenstein.txt")
    # print(content)
    
    word_count = get_num_words(content)

    print(f"Found {word_count} total words")

    num_of_character = get_num_character(content)

    print("num of character dictionary")


    print(num_of_character)

if __name__ == "__main__":
    main()
