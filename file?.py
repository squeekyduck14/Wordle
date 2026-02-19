from pathlib import Path
# Change 1 : Something must be initialized here
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

def user_guess(word_bank):
	guess = input("Enter a 5 letter word: ").strip().lower()
	# the strip function removes whitespace from strings
	# the lower function makes all characters lowercase
	if len(guess) != 5:
		# != means not equals
		print("You made a mistake, word submission must be 5 letters long. ")
	elif guess not in word_bank:
		# not in allows us to compare strings within arrays
		print("That's not a real word. You should feel bad. ")
	else:
		return guess

def main():
	print("Wordle Test Project")
	words = load_word_bank(word_file)
	# Change 2 : Needs a way to call a random sample and print i
	sample = random.choice(words)
	guess = user_guess(words)
	print(f"Your guess was {guess}, the word was {sample}")

if __name__ == "__main__":
	main()
