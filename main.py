"""
Name(s): Ayden and Justin
Name of Project: It's Time to Play HANGMAN!
"""
import time
import random
import page1
import page2
from page1 import stages
from page2 import list

print("H-A-N-G-M-A-N: By Justin Lin and Ayden Gillian")
time.sleep(1)
yes = "yes"
Yes = "Yes"
YES = "YES"
hi = "no"
hi = input("Do you want to play Hangman? ")
while hi != yes and hi!= Yes and hi != YES:
  hi = input("Awww are you sure? Do you want to play Hangman? ")
if hi == yes or Yes or YES:
  print("Let's start!")
  


hang_word = random.choice(list)
hang_length = len(hang_word)

lost_game = False
numlives = 7

print("_ " * hang_length)
HANGMAN = []
for _  in range(hang_length):
  HANGMAN += "_"
while not lost_game:
  guess = input("Enter a letter: ").lower()
  if guess in HANGMAN:
    print(f"You have already guess '{guess}'")
    guess = input("Guess a letter:").lower()
  for position in range(hang_length):
    letter = hang_word[position]
    if letter == guess:
      HANGMAN[position] = letter 
      print("You've got a letter!")
      
  if guess not in hang_word:
    print(f"The letter {guess} is not in the word :(")
    numlives -= 1
    if numlives == 0:
        lost_game = True
        print("Aw man...you lose")
        print(f"The word was: {hang_word}")

  print(f"{''.join(HANGMAN)}")
  if "_" not in HANGMAN:
      lost_game = True
      print("CONGRATS! You've beat the game!")

  print(stages[numlives])
