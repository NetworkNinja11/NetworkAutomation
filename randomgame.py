
# python program to guess random number...

import random  # This helps to import random package....

max_number = int(input("Enter the max number upto which you want to guess: "))

ran = random.randint(1, max_number) #This helps to generate random number between 1 and the highest number upto which the user want to guess

guess = int(input("Enter your guess number between 1 to {}: ".format(max_number))) #It is the guess value the user want to enter...
2
if guess == ran:
    print("You guessed it correct in the first guess...!!!!")
count = 1
while guess != ran:
    count+= 1
    guess2 = int(input("Enter your guess again: "))
    if guess2 == ran:
        print("finally, you guessed it right and it took you", count, "attempts.")
        break
print("Thanks! for playing our random game...hope you play this game again and again..")








