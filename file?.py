
# hard code approach - most direct


from pathlib import Path
word_file = Path("5-letter-word.txt")

def file_word_file():
    if word_file.exists():
        return word_file
    else:
        print(" Error - File not found :( ")
    

# Using a refernce document approach 
def load_word_bank (filename = "5-letter-word.txt"):
     with open(filename, "r") as file: 
         return [line.strip().lower() for line in file if len(line.strip()) == 5]
 
         
word_file = load_word_bank()


def main():
    print("Wordle Test Project")
    # using the word_file call on a random element in the file