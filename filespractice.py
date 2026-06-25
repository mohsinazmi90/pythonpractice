# [Start Program]
#        ▼
# 1. READ: Open 'highscore.json' in "r" mode.
#    (Load the number inside into a variable named 'current_highscore')
#        ▼
# 2. SHOW & ASK: Print the current high score.
#    Ask the user: "What was your score this game?"
#        ▼
# 3. COMPARE: If the new score is bigger than 'current_highscore',
#    update the variable.
#        ▼
# 4. WRITE: Open 'highscore.json' in "w" mode.
#    (Dump the updated high score back into the file)
#        ▼
# [End Program]

import json
import os


def main():
    if os.path.exists("highscore.json"):
        with open("highscore.json", "r") as file:
            current_highscore = json.load(file)
    else:
        current_highscore = 0

    print(f"The current high score is: {current_highscore}")

    # 1. Ask the user for their new score
    new_score = int(input("Enter your score from this game: "))

    if new_score > current_highscore:
        print("🎉 New High Score!")
        current_highscore = new_score

        # 3. Open the file in "w" (write) mode to save the updated score
        with open("highscore.json", "w") as file:
            json.dump(current_highscore, file)
    else:
        print("Good try, but you didn't beat the high score.")


if __name__ == "__main__":
    main()
