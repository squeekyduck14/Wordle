from pathlib import Path

# Change 1: need to include random library
import random

word_file = Path("5-letter-words.txt")

def find_word_file():
	if word_file.exists():
		return word_file
	else:
		print(" Error - File not found! :( ")

# Using a reference document approach
def load_word_bank (filename = "5-letter-words.txt"):
	with open(filename, "r") as file:
		return [line.strip().lower() for line in file if len(line.strip()) == 5]
	
word_bank = load_word_bank()

def main():
	print("Wordle Test Project")
	# Change 2: 
	words = load_word_bank(word_file)
	sample  = random.choice(words)
	print(f"Test Sample Word: {sample}")

# Change 3: Need to run main function, so that is written below
if __name__ == "__main__":
	main()
