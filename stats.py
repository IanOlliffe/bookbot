def get_book_text(path_to_book):
    with open(path_to_book) as book_contents:
        return book_contents.read()
    
def count_words(book_text):
    return len(book_text.split())

def get_num_words(book_path):
    word_count = count_words(get_book_text(book_path))
    print(f"Found {word_count} total words")

def count_characters(book_text):
    # standardize book text to lowercase to avoid repeat letters (eg p: 1, P: 4. we want p: 5)
    lowercase_book_text = book_text.lower()
    character_counts = {}
    for character in lowercase_book_text:
        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1
    return character_counts

def sort_on(dict_item):
    return dict_item["num"]

def sort_characters(character_counts):
    sorted_list = []
    for char, num in character_counts.items():
        if char.isalpha():
            new_entry_to_unsorted_list = {"char": char, "num": num}
            sorted_list.append(new_entry_to_unsorted_list)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_character_counts(book_path):
    character_counts = sort_characters(count_characters(get_book_text(book_path)))
    for item in character_counts:
            print(f"{item['char']}: {item['num']}")