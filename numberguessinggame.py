import random as rnd

def game(upper,lower):
    score=0
    print('Think of a number between ' ,lower, ' and ',upper)
    isCorrect = False
    while isCorrect == False:
     guess =rnd.randint(lower,upper) 
     score+=1
     print("I guess " + str(guess) + "."+" Is it correct. Should I guess another number higher or lower.")

     response = input().lower()
     if response == 'correct' or response == 'c':
      isCorrect = True
      print('The correct score is ',score)
     elif response == 'higher' or response == 'h':
      lower = guess+1
     elif response == 'lower' or response == 'l':
       upper = guess-1

     

    return score


print("Welcome to the game..")

upper = input("Enter your upper number: ")
lower = input("Enter your lower number: ")

while (upper.isdigit() == False) or (lower.isdigit() == False):
    print('These MUST BE positive integers:')
    upper = input("Enter your upper number again: ")
    lower = input("Enter your lower number again: ")

score = game(int(upper),int(lower))