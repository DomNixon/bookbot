from stats import num_words
from stats import num_char

def book_capture():
	with open("books/frankenstein.txt") as f:
		file_content = f.read()
		return file_content


def main ():

	print(f"Found {num_words(book_capture())} total words")
	print(num_char(book_capture()))
main()
