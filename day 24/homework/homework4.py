import random 

number_to_guess = random.randint(1, 10)

tries = 3

while tries > 0:
    guess = int(input("Guess a number from 1 to 10: "))

    if guess == number_to_guess:
        print("You win!")
        break  
    else:
        tries -= 1  
        if tries > 0:
            print("Wrong number. Tries left:", tries)  
        else:
            print("You lose. The correct number was:", number_to_guess)  

