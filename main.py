import sys
from stats import (
	word_count,
	get_book_text,
	char_count,
	dict_list,
)

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)	
	content = get_book_text(sys.argv[1])
	count = word_count(content)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {sys.argv[1]}...")
	print("----------- Word Count ----------")
	print(f"Found {count} total words")
	print("--------- Character Count -------")
	character_count = char_count(content)
	sorted_list = dict_list(character_count)
	for character_dict in sorted_list:
		if character_dict["char"].isalpha():
			print(f"{character_dict["char"]}: {character_dict["count"]}")
	print("============= END ===============")

main()