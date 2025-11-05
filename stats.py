
alphabet = "abcdefghijklmnopqrstuwxyzáäàæéèëóòöúùüãõñêâôû"


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def word_counter(text):
    
    words = text.split()
    word_count = len(words)
    return word_count

def letter_counter(words):
    formatted_words = words.lower()
    letter_dict = {}

    for letter in alphabet:
        counter = 0
        for i in formatted_words:
            if i == letter:
                counter = counter + 1            
            
            else:
                continue

        letter_dict[letter] = counter
    
    return letter_dict

def sorted_dic(dic):
    return dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))

def list_of_values(dic):
    return list(dic.values())

def list_of_letters(dic):
    return list(dic.keys())

def letter_num_pairing(keys, values):
    for i in range(len(keys)):
        print(f"{keys[i]}: {values[i]}")



