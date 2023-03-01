import requests
import json
import random
import re

# API request which turns JSON file into string
difficulty = input("Difficulty (easy, medium, or hard): ")
if difficulty == "easy":
    number = str(random.randint(4, 6))
    word_request = requests.get("https://random-word-api.herokuapp.com/word?length=" + number)
elif difficulty == "medium":
    number = str(random.randint(7, 10))
    word_request = requests.get("https://random-word-api.herokuapp.com/word?length=" + number)
elif difficulty == "hard":
    number = str(random.randint(11, 15))
    word_request = requests.get("https://random-word-api.herokuapp.com/word?length=" + number)
else:
    word_request = requests.get("https://random-word-api.herokuapp.com/word?length=")

# Converts json into readable string
word = json.loads(word_request.text)
word = json.dumps(word)
word = word[2:-2]
# print(word)

decompsed_word = list(word)
# print(decompsed_word)

# Length
length = len(word)
print(f"{length} characters")
print()

# Prints the spaces for player.
play_area = ["_"]
play_area = play_area * length

# Starts off the player with 8 lives.
player_lives = 8
print(f"You have {player_lives} lives")

print(play_area)

# Checks for input letter against the generated word
# Shows letter in the play area
# Counts lives accordingly
while player_lives != 0:

    player_guess = input("Letter: ")
    if player_guess in word:
        for letter in re.finditer(player_guess, word):
            guess_location = letter.start()
            play_area[guess_location] = player_guess
        print("Yes")
        if play_area == decompsed_word:
            print("You win!")
            break
    else:
        player_lives -= 1
        print("No")

    print()
    print(f"{player_lives} lives remain")
    print(play_area)

# Prints word at the very end
print(f"The word was {word}")
