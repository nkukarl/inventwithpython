import random
hangmanpics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

word = words[random.randrange(0, len(words))]

print(word)

def add_underline(string):
  new_string = ""
  for i in string:
    new_string += i
    new_string += " "
  return new_string

missed_letters = ""
guess_result = "_" * len(word)

cnt = 0

print hangmanpics[cnt]
print add_underline(guess_result)
print "missed letter: ", missed_letters

while cnt < 6:
  print("**********************************")
  # guessed_letter = input("Guess a letter: ")
  guessed_letter = chr(random.randrange(97, 123))
  print guessed_letter
  new_guess_result = ""
  if guessed_letter in word:
    for i in range(0, len(word)):
      if word[i] == guessed_letter:
        new_guess_result += guessed_letter
      else:
        new_guess_result += guess_result[i]
    guess_result = new_guess_result
  else:
    missed_letters += guessed_letter
    cnt += 1
  print hangmanpics[cnt]
  print add_underline(guess_result)
  print "missed letter: ", missed_letters
  if guess_result == word:
      print("You win!")
      break
else:
  print("You lose!")
