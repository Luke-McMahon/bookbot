
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    letters = get_letter_count(text)
    report = get_document_report(book_path, word_count, letters)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())

def get_letter_count(text):
    letters = {}
    lowered = text.lower()

    for char in lowered:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    return letters

def sort_by(d):
    return d["num"]

def sort_dict(letters):
    sorted_list = []
    for letter in letters:
        sorted_list.append({"letter": letter, "num": letters[letter]})
    sorted_list.sort(reverse=True, key=sort_by)
    return sorted_list

def get_document_report(book_path, word_count, letters):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")

    sorted = sort_dict(letters)

    for letter in sorted:
        if letter["letter"].isalpha():
            print(f"The '{letter['letter']}' was found {letter['num']} times")

    print("\n--- End report ---")

if __name__ == "__main__":
    main()
