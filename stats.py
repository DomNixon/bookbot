def num_words(text):
	word_list = text.split()
	total = len(word_list)
	return total


def num_char(text):
	char_count = {}
	ltext = text.lower()
	for char in ltext:
		if char in char_count:
			char_count[char] += 1
		else:
			char_count[char] = 1
	return char_count