import random
number = random.randint(0,9)
chances = 5
print("Guess a number between 0 and 9:")
guess = int(input("your guess:  "))


while chances >-1: 
    if  chances == 0:
        print("Oh No! The number was ",number,". Better Luck Next Time")
        break
    elif (guess<number):
        print ("your guess was too low. Try a number greater than ", guess )
        chances = chances-1
        guess = int(input("your guess:  "))

    elif (guess>number):
        print("your guess was too high. Try a number less than ", guess)
        chances = chances-1
        guess = int(input("your guess:  "))

    elif (guess==number):
        print("Congratulations you WON!!!")
        break

    



