import random

def secret_number_generation():
    all_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    secret_number = ''
    digits = 3
    i = 0
    while i < digits:
        rand_index = random.randrange(0, len(all_numbers))
        digit = all_numbers[rand_index]
        all_numbers.pop(rand_index)
        secret_number += digit
        i += 1
    return secret_number
    
def clue_generation(secret_number, guess_number):
    clue = []
    if secret_number == guess_number:
        return "You got it!"
    for i in range(len(guess_number)):
        if guess_number[i] == secret_number[i]:
            clue.append("Fermi")
        elif guess_number[i] in secret_number:
            clue.append("Pico")
        clue.sort()
        
    if len(clue) == 0:
        clue.append("Bagels")
    return ' '.join(clue)

def check_guess_number_general(guess_number):
    if len(guess_number) != 3:
        print("Wrong length!")
        return False
    for i in guess_number:
        if i < '0' or i > '9':
            print("Not a number!")
            return False
    return True
            
def check_guess_number_uniqueness(guess_number):
    guess_number = list(guess_number)    
    temp = []
    for i in guess_number:
        if i not in temp:
            temp.append(i)
    if temp == guess_number:
        return True
    else:
        print("Unique digits!")
        return False

to_play = True
while to_play:
    secret_number = secret_number_generation()
    print(secret_number)
    
    guess_remain = 5
    guess_id = 1
    while guess_id <= guess_remain:
        check_guess = False    
        while not check_guess:   
            guess_number = input("Guess #" + str(guess_id) + "\n")
            check_guess = check_guess_number_general(guess_number) and check_guess_number_uniqueness(guess_number)
        clue = clue_generation(secret_number, guess_number)
        print(clue)
        if clue == "You got it!":
            break
        guess_id += 1
    else:
        print("You lost!")
    to_play_choice = input("Continue to play? (y/n) ")
    to_play = (to_play_choice == 'y')
