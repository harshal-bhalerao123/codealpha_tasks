import random

def hangman():
    words = ["python", "programming", "hangman", "developer", "internship"]
    word = random.choice(words)  
    guessed_word = ["_"] * len(word)  
    guessed_letters = []  
    attempts = 6 

    print("Welcome to Hangman Game!")
    print("Guess the word:")
    print(" ".join(guessed_word))

    while attempts > 0 and "_" in guessed_word:
        guess = input("\nEnter a letter: ").lower()

        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Enter a single alphabet.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

      
        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f"Wrong guess! '{guess}' is not in the word.")
            print(f"Attempts remaining: {attempts}")

        print(" ".join(guessed_word))

    if "_" not in guessed_word:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nGame over! The word was:", word)


if __name__ == "__main__":
    hangman()