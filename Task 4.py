import random

# Word List
word_list = ["python", "hangman", "programming", "computer", "learning", "challenge"]

def choose_random_word(word_list):
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman_display(incorrect_guesses):
    hangman_figures = [
        """
        +---+
        |   |
            |
            |
            |
            |
        ============
        """,
        """
        +---+
        |   |
        O   |
            |
            |
            |
        ============
        """,
        """
        +---+
        |   |
        O   |
        |   |
            |
            |
        ============
        """,
        """
        +---+
        |   |
        O   |
       /|   |
            |
            |
        ============
        """,
        """
        +---+
        |   |
        O   |
       /|\\  |
            |
            |
        ============
        """,
        """
        +---+
        |   |
        O   |
       /|\\  |
       /    |
            |
        ============
        """,
        """
        +---+
        |   |
        O   |
       /|\\  |
       / \\  |
            |
        ============
        """
    ]
    return hangman_figures[incorrect_guesses]

def main():
    print("Welcome to Hangman!")

    while True:
        word = choose_random_word(word_list)
        guessed_letters = []
        incorrect_guesses = 0

        while incorrect_guesses < len(hangman_display(0)):
            print(hangman_display(incorrect_guesses))
            print(display_word(word, guessed_letters))

            if "_" not in display_word(word, guessed_letters):
                print("You win! The word was:", word)
                break

            guess = input("Guess a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue

            if guess in guessed_letters:
                print("You've already guessed that letter.")
                continue

            if guess in word:
                guessed_letters.append(guess)
            else:
                incorrect_guesses += 1

        if incorrect_guesses >= len(hangman_display(0)):
            print(hangman_display(incorrect_guesses))
            print("You lose! The word was:", word)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Thanks for playing Hangman!")

if __name__ == "__main__":
    main()
