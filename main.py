from stats import get_num_words, get_character_counts
import sys

def main():
    if len(sys.argv) == 2:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        get_num_words(sys.argv[1])
        print("--------- Character Count -------")
        get_character_counts(sys.argv[1])
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()