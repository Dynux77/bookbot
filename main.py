

import sys

from stats import word_counter
from stats import get_book_text
from stats import letter_counter
from stats import list_of_values
from stats import list_of_letters
from stats import letter_num_pairing
from stats import sorted_dic

if len(sys.argv) < 2:
   print("Usage: python3 main.py <path_to_book>")
   sys.exit(1)
else: 
   file_path = sys.argv[1]

   

def main():
   num_words = word_counter(get_book_text(file_path))
   letter_count = letter_counter(get_book_text(file_path))
   sorted_letters_nums = sorted_dic(letter_count)
   letter_list = list_of_letters(sorted_letters_nums)
   sorted_count = list_of_values(sorted_letters_nums)


   print("============ BOOKBOT ============")
   print(f"Analyzing book found at {file_path}...")
   print("----------- Word Count ----------")
   print(f"Found {num_words} total words")
   print("--------- Character Count -------")
   letter_num_pairing(letter_list, sorted_count)

   print(sys.argv)

   

   

   


main()