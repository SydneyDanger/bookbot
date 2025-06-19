import sys
from stats import count_words, count_characters, sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]

        text = get_book_text(filepath)
        word_count = count_words(text)
        character_count = count_characters(text)
        sorted_characters = sort_dict(character_count)

        # print the report
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for dict in sorted_characters:
            if dict['char'].isalpha():
                print(f"{dict['char']}: {dict['num']}")

main()