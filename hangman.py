import random
import simplegui
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def add_underline(string):
  new_string = ""
  for i in string:
    new_string += i
    new_string += " "
  return new_string

def guess_a_letter(guess):
    global correct_input, guessed_letter, cnt, guessed_letters, word, missed_letters, guess_result, warning_msg, result_msg, hangmanpic, guess_result_str, missed_letters_str, image
    if result_msg == "":
        if cnt < 6: 
            correct_input = False
            if len(guess) != 1:
                warning_msg = "*ONLY ONE* letter!"
            elif not ('a' <= guess.lower() <= 'z'):
                warning_msg = "a *LETTER*!"
            elif guess in guessed_letters:
                warning_msg = "Already guessed!"
            else:
                guessed_letters += guess.lower()
                warning_msg = ""
                correct_input = True
            
            if correct_input:  
                new_guess_result = ""
                if guess in word:
                    for i in range(0, len(word)):
                        if word[i] == guess:
                            new_guess_result += guess
                        else:
                            new_guess_result += guess_result[i]
                    guess_result = new_guess_result
                else:
                    missed_letters += guess
                    cnt += 1        
        image = simplegui.load_image("https://dl.dropboxusercontent.com/u/52743103/hangman/hangman" + str(cnt) + ".jpg")
        guess_result_str = add_underline(guess_result)
        missed_letters_str = "Missed letter: " + missed_letters
        if guess_result == word:
            result_msg = "You win!"
        elif cnt == 6:
            result_msg = "You lose!"
        
def new_game():
    global cnt, guessed_letters, word, missed_letters, guess_result, warning_msg, result_msg, hangmanpic, guess_result_str, missed_letters_str, image
    word = words[random.randrange(0, len(words))]
    guessed_letters = ""
    
    print(word)
    
    missed_letters = ""
    guess_result = "_" * len(word)
    
    cnt = 0
    
    image = simplegui.load_image("https://dl.dropboxusercontent.com/u/52743103/hangman/hangman0.jpg")
    guess_result_str = add_underline(guess_result)
    missed_letters_str = "Missed letter: " + missed_letters
    
    warning_msg = ""
    result_msg = ""
    
    
def draw(canvas):
    canvas.draw_text(warning_msg, [100, 50], 36, "red")
    canvas.draw_text(result_msg, [100, 100], 36, "blue")
    canvas.draw_image(image, (960 / 2, 720 / 2), (960, 720), (170, 200), (150, 150))
    canvas.draw_text(guess_result_str, [100, 310], 36, "yellow")
    canvas.draw_text(missed_letters_str, [100, 360], 36, "green")
    
        
frame = simplegui.create_frame("Hangman", 500, 400)

frame.set_draw_handler(draw)

frame.add_input("Guess a letter", guess_a_letter, 100)
frame.add_button("New game", new_game, 100)

frame.start()

new_game()
