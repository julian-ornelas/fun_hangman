import requests
import json
import random
import re

# API request
Length = input("Length (short, medium, or long): ")
if Length == "short":
    number = str(random.randint(4, 6))
    word_request = requests.get("https://random-word-api.herokuapp.com/word?length=" + number)
elif Length == "medium":
    number = str(random.randint(7, 10))
    word_request = requests.get("https://random-word-api.herokuapp.com/word?length=" + number)
elif Length == "long":
    number = str(random.randint(11, 15))
    word_request = requests.get("https://random-word-api.herokuapp.com/word?length=" + number)
else:
    word_request = requests.get("https://random-word-api.herokuapp.com/word")

# Converts json into readable string
word = json.loads(word_request.text)
word = json.dumps(word)
word = word[2:-2]

decompsed_word = list(word)

# word_length
word_length = len(word)
print(f"{word_length} characters")
print()

# Prints the spaces for player.
play_area = ["_"]
play_area = play_area * word_length

# Starts off the player with 8 lives.
player_lives = 8
print(f"You have {player_lives} lives")

print(play_area)

# Checks for input letter against the generated word
# Shows letter in the play area
# Counts lives accordingly
guessed_letters = []
while player_lives != 0:

    player_guess = input("Letter: ")
    if len(player_guess) > 1:
        print("Just one letter")
    elif len(player_guess) == 0:
        print("Type a letter")
    else:
        if player_guess in guessed_letters:
            print("You used this already")
            
        else:
            if player_guess in word:
                for letter in re.finditer(player_guess, word):
                    guess_location = letter.start()
                    play_area[guess_location] = player_guess
                print("Yes")
                if play_area == decompsed_word:
                    print()
                    print("You win!")
                    break
            else:
                player_lives -= 1
                print("No")
                if player_lives == 0:
                    print()
                    print("You lost")
                    break
            guessed_letters = guessed_letters + list(player_guess)

    print()
    print(f"{player_lives} lives remain")
    print(play_area)
    print(f"Guessed letters: {guessed_letters}")

# Prints word at the very end
print(f"The word was {word}")

#Test
