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
def add_underline(string):
  new_string = ""
  for i in string:
    new_string += i
    new_string += " "
  return new_string

def check_input(string):
    global guessed_letters
    if len(string) != 1:
        print("*ONLY ONE* letter!")        
        return True
    elif not ('a' <= string.lower() <= 'z'):
        print("a *LETTER*!")
        return True
    elif string in guessed_letters:
        print("Already guessed!")
        return True
    else:
        guessed_letters += string.lower()
        return False

to_play = True

while to_play:
    word = words[random.randrange(0, len(words))]
    
    guessed_letters = ""
    
    print(word)
    
    missed_letters = ""
    guess_result = "_" * len(word)
    
    cnt = 0
    
    print(hangmanpics[cnt])
    print("Guess a", len(word), "letter word.")
    print(add_underline(guess_result))
    print("missed letter: ", missed_letters)
    
    while cnt < 6:
      print("**********************************")
      input_flag = True
      while input_flag:
          guessed_letter_temp = input("Guess a letter: ")
          input_flag = check_input(guessed_letter_temp)
      # guessed_letter = chr(random.randrange(97, 123))
      guessed_letter = guessed_letter_temp.lower()
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
      print(hangmanpics[cnt])
      print(add_underline(guess_result))
      print("missed letter: ", missed_letters)
      if guess_result == word:
          print("You win!")
          break
    else:
      print("You lose!")
    
    user_choice = input("Continue to play? (y/n) ")
    if user_choice == "n":
        to_play = False
