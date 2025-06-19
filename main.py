import sys
from stats import get_num_words
from stats import get_character_frequency

def get_book_text(filepath):
    with open(filepath) as f:
      file_content = f.read()
    return file_content

def main():
    if len(sys.argv) < 2:
      print("Usage: python3 main.py <path_to_book>")
      sys.exit(1)
    else:
      filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(get_num_words(filepath))
    print("--------- Character Count -------")
    char_count = get_character_frequency(filepath)
    for item in char_count:
      print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()