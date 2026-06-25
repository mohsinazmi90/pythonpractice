from random_word import RandomWords

r = RandomWords()


def generate_word():
    word = r.get_random_word()
    return word


def hangman_game(word):

    hidden = ["_"] * len(word)
    count = 0
    letters_guessed = []

    while True:
        print("Word:", " ".join(hidden))
        print(f"Guesssed letters: ", " ".join(letters_guessed).upper())

        guess = input("\nEnter your guess: ").lower().strip()

        if len(guess) != 1:
            print("Enter one letter at a time")
            continue

        if not guess.isalpha():
            print("Use Alphabets only")
            continue

        if guess not in letters_guessed:
            letters_guessed.append(guess)
        else:
            print("You already guessed this letter")
            continue

        if guess not in word:
            count += 1
            print(f"Life {count} of 6 used")

        if count == 6:
            print(f"You lost! The word was {word}")
            break

        for i in range(len(word)):
            if word[i] == guess:
                hidden[i] = guess

        if "".join(hidden) == word:
            print("You guessed the word:", word)
            break


def main():
    word = generate_word()
    hangman_game(word)


if __name__ == "__main__":
    main()
