def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()

def word_count(content):
	words = content.split()
	return len(words)

def char_count(content):
	lowercase = content.lower()
	char_dict = dict()
	for ch in lowercase:
		if ch in char_dict:
			char_dict[ch] += 1
		else:
			char_dict[ch] = 1
	return char_dict

def sort_on(dictionary):
	return dictionary["num"]

def sort_dict(dictionary):
	new_list = list()
	for ch, count in dictionary.items():
		new_list.append({"char": ch, "num": count})
	new_list.sort(reverse=True, key=sort_on)
	return new_list