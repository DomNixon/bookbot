from stats import num_words
from stats import num_char
from stats import sorted_alpha_num_char

def book_capture():
	with open("books/frankenstein.txt") as f:
		file_content = f.read()
		return file_content

def main ():
	book_text = book_capture()
	print("============ BOOKBOT ============")
	print("Analyzing book found at books/frankenstein.txt...")
	print("----------- Word Count ----------")
	print(f"Found {num_words(book_text)} total words")
	print("--------- Character Count -------")
	counts = num_char(book_text)
	sorted_alpha_num_char(counts)
	print("============= END ===============")

main()
