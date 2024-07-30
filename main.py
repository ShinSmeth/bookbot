def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    word_number = word_count(file_contents)
    char_frequencies = char_count(file_contents)
    
    print(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_number} words found in the document")
    
    for char, count in sorted(char_frequencies.items(), key=lambda item: item[1], reverse=True):
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

def word_count(words):
    word_list = words.split()
    word_number = len(word_list)
    return word_number

def char_count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered.isalpha():  # Consider only alphabetic characters
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars

main()