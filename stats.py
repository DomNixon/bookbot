def num_words(text):
	word_list = text.split()
	return len(word_list)


def num_char(text):
	char_count = {}
	ltext = text.lower()
	for char in ltext:
		if char.isalpha():
			if char in char_count:
				char_count[char] += 1
			else:
				char_count[char] = 1
	return char_count

def sorted_alpha_num_char(text):
	sorted_items = sorted(
        text.items(),
        key=lambda item: item[1],
        reverse=True
    )
	for char, num in sorted_items:
			print(f"{char}: {num}")