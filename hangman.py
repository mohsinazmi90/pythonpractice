from wonderwords import RandomWord

def random_word():
    rw = RandomWord()
    word = rw.word()
    return word
    
def letter_guess(word):
    game = '_' * len(word)
    count = 0
    letter_guessed = []
    
    try:
        while True:
            print("Word: ", " ".join(game))
            letter = input("Guess your letter: ").lower()
            
            if len(letter) != 1:
                print("Single letters only")
                continue
            
            if letter in letter_guessed:
                print(f"Guessed letters:", ", ".join(letter_guessed))
                continue
            else:
                letter_guessed.append(letter)

                        
            if letter in word:
                new_game = ""
                for index, char in enumerate(word):
                    if char == letter:
                        new_game += letter
                    else:
                        new_game += game[index]
                game = new_game
            else:
                count += 1
                print(f"Letter is not in word. You are on try number {count}")
            
            if game == word:
                print(f"You guessed it. The word was '{game}'")
                break
            
            if count > 6:
                print(f"Game over! The word was '{word}'")
                break
    except:
        print("Guess only single letters...")
        
    
    
def main():
    word = random_word()
    letter_guess(word)
    
if __name__ == "__main__":
    main()
    
    