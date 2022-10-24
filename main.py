from ast import main
import random
import time

counter = 0

def checkNum(num):
    
    global counter 
    counter+=1
    try:
        guess_num= int(input("Guess a number between 1 to 100: "))
    except Exception as e:
        print("You are required to enter a number to play this game")
        checkNum(num)
    try:
        if guess_num>num:
            print("Try a LOWER number")
            checkNum(num)
        elif guess_num<num:
            print("Choose a HIGHER number")
            checkNum(num)
        else:
            print("Correct!!!!")
            time.sleep(1)
            print(f"Prefectly guessed at guess number {counter}")
    except Exception as e:
        print("")

if __name__ == "__main__":
    number = random.randrange(1,100,1)
    print("Are you ready to play??")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("Let's play The Guessing Game!")
    checkNum(number)
