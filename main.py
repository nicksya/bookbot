import sys

from stats import get_num_words
from stats import get_book_stats_sorted

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path_to_file = sys.argv[1]
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    
    num_words = get_num_words(path_to_file)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    book_stats = get_book_stats_sorted(path_to_file)
    print("--------- Character Count -------")
    for stat in book_stats:
        print(f"{stat["char"]}: {stat["num"]}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
