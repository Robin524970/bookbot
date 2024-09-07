def main() :
    file_path = "books/frankenstein.txt"
    file_contents = get_file_contents(file_path)

    char_count_dict = char_count(file_contents)
    char_count_list = dict_list(char_count_dict)
    char_count_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count(file_contents)} words found in the document\n")

    for dict in char_count_list:
        print(f"The \'{dict['char']}\' character was found {dict['count']} times ")

    print("--- End report ---")

def sort_on(dict):
    return dict["count"]

def dict_list(dict):
    char_count_list = []
    for k, v in dict.items():
        current_char = {
            "char": k,
            "count": v
        }
        char_count_list.append(current_char)
    return char_count_list

def word_count(content):
    words = content.split()
    return len(words)

def char_count(content):
    lowercase = content.lower()
    result_dict = {}
    for character in  [chr(i) for i in range(97, 123)]:
        result_dict[character] = lowercase.count(character)
    return result_dict

def get_file_contents(file_path):
    with open(file_path) as f:
        return f.read()
    

main()