def sort_on(dict):
    return dict["num"]

def open_file(path):
    with open(path) as f:
        file_content = f.read()
    return file_content

def words_count(file):
    words = file.split()
    return len(words)

def words_to_char_dict(file):
    char_dict = {}
    for word in file:
        lowered = word.lower()
        for char in lowered:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def dict_to_sorted_list(dict):
    unsorted_list = []
    for char in dict:
        if char.isalpha():  
            unsorted_list.append({"char": char, "num": dict[char]})
    
    unsorted_list.sort(reverse=True, key=sort_on)
    print(unsorted_list)
    return unsorted_list
            
            
def main():
    path = "books/frankenstein.txt"
    file_content = open_file(path)
    words_num = words_count(file_content)
    char_dict = words_to_char_dict(file_content)
    sorted_char_list = dict_to_sorted_list(char_dict)
    
    print(f"--- Begin report of {path} ---")
    print(f"{words_num} words found in the document")
    print()
    for i in range(len(sorted_char_list)):
        print(f"The '{sorted_char_list[i]['char']}' character was found {sorted_char_list[i]['num']} times")
    
main()