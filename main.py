def main():
    
    try:
        book_path = "books/frankenstein.txt"
        book_text = get_book_text(book_path)
        word_count = get_word_count(book_text)
    except Exception as e:
        print("Doit run main du terminal pour avoir bon book path")
    
    num_each_letter= count_each_letter(book_text)
    num_each_letter.sort(reverse=True, key=sort_on)
    print_report(word_count, num_each_letter, book_path)

def print_report(num_words, num_each_letter, book_path):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words have been found in the document.")
    for index in range (0, len(num_each_letter)):
        print(f"The {num_each_letter[index]['letter']} character was found {num_each_letter[index]['num']} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["num"]

def count_each_letter(text): #Returns a list of dicts [{"letter": "a", "num": 0}, {"letter": "b", "num": 0},...]
    text = text.lower()
    output = [
        {"letter": "a", "num": 0},
        {"letter": "b", "num": 0},
        {"letter": "c", "num": 0},
        {"letter": "d", "num": 0},
        {"letter": "e", "num": 0},
        {"letter": "f", "num": 0},
        {"letter": "g", "num": 0},
        {"letter": "h", "num": 0},
        {"letter": "i", "num": 0},
        {"letter": "j", "num": 0},
        {"letter": "k", "num": 0},
        {"letter": "l", "num": 0},
        {"letter": "m", "num": 0},
        {"letter": "n", "num": 0},
        {"letter": "o", "num": 0},
        {"letter": "p", "num": 0},
        {"letter": "q", "num": 0},
        {"letter": "r", "num": 0},
        {"letter": "s", "num": 0},
        {"letter": "t", "num": 0},
        {"letter": "u", "num": 0},
        {"letter": "v", "num": 0},
        {"letter": "w", "num": 0},
        {"letter": "x", "num": 0},
        {"letter": "y", "num": 0},
        {"letter": "z", "num": 0}
    ]
    for a in text:
        if a.isalpha():
            for i in range(0, len(output)):
                if output[i]["letter"]==a:
                    output[i]["num"]+=1 
        

    return output

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(text):
     return len(text.split())

main()

