def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def word_counter(text):
    
    words = text.split()
    word_count = len(words)
    return word_count