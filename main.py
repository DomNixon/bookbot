def book_capture():
	with open("books/frankenstein.txt") as f:
		file_content = f.read()
		return file_content


def num_words(text):
	word_list = text.split()
	total = len(word_list)
	return total



def main ():

	print(f"Found {num_words(book_capture())} total words")

main()