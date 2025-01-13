def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_num_character(text)
    sorted_chars_list = chars_dict_to_list(chars_dict)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()

    for item in sorted_chars_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_character(text):
    count = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

def sort_on(d):
    return d["num"]

def chars_dict_to_list(num_chars_dict):
    sorted_chars = []
    for char in num_chars_dict:
        sorted_chars.append({"char": char, "num": num_chars_dict[char]})
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars

main()