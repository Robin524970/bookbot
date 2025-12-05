from stats import word_count, char_count, sort_dict
import sys

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	file_path = sys.argv[1]
	frank = get_book_text(file_path)
	num_of_words = word_count(frank)
	num_of_char = sort_dict(char_count(frank))

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {file_path}...")
	print("----------- Word Count ----------")
	print(f"Found {num_of_words} total words")
	print("--------- Character Count -------")

	for dictionary in num_of_char:
		char = dictionary["char"]
		num = dictionary["num"]
		if char.isalpha():
		    print(f"{char}: {num}")

	print("============= END ===============")

def get_book_text(filepath):
	with open(filepath) as file:
		file_contents = file.read()
	return file_contents

main()