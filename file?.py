from pathlib import Path
import random

word_file = Path("5-letter-words.txt")

def load_word_bank(filename=word_file):
    with open(filename, "r") as file:
        return [line.strip().lower() for line in file if len(line.strip()) == 5]

def user_guess(word_bank):
    while True:
        guess = input("Enter a 5 letter word: ").strip().lower()
        if len(guess) != 5:
            print("Word submission must be 5 letters long.")
        elif guess not in word_bank:
            print("That's not a real word.")
        else:
            return guess

def score_guess(guess: str, target: str):
    
    result = ["B"] * 5
    target_chars = list(target)

    
    for i in range(5):
        if guess[i] == target[i]:
            result[i] = "G"
            target_chars[i] = None

    for i in range(5):
        if result[i] == "B" and guess[i] in target_chars:
            result[i] = "Y"
            target_chars[target_chars.index(guess[i])] = None


    for i in range(5):
        if result[i] in ("G", "Y"):
            if target.count(guess[i]) > guess.count(guess[i]):
                result[i] = "O"

    return result

def emoji_feedback(score):
    emoji_map = {"G": "🟩", "Y": "🟨", "B": "⬛", "O": "🟧"}
    return "".join(emoji_map[s] for s in score)

def print_legend():
    print("🟩 Correct position")
    print("🟨 Wrong position")
    print("🟧 Right/wrong position — but another copy of this letter is still hiding")
    print("⬛ Not in word\n")

def main():
    print("Wordle Test Project (Emoji Board)\n")
    print_legend()
    words = load_word_bank(word_file)
    target = "trees"
    board = []

    for attempt in range(1, 7):
        guess = user_guess(words)
        score = score_guess(guess, target)
        board.append(emoji_feedback(score))

        print("\nCurrent Board:")
        for row in board:
            print(row)
        print()

        if guess == target:
            print(f"You got it in {attempt} guess{'es' if attempt > 1 else ''}!")
            return

    print(f"Out of guesses. The word was: {target}")

if __name__ == "__main__":
    main()
