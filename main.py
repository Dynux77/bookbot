
from stats import word_counter
from stats import get_book_text

def main():
   num_words = word_counter(get_book_text("books/frankenstein.txt"))
   print(f"Found {num_words} total words")


main()