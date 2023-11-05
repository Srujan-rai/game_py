import random

def predict(num):
    random_number=random.randint(1,num)
    guess = 0
    while guess!=random_number:
        guess=int(input("enter the number: "))
        print(guess)
        if guess < random_number:
            print("too low")
        elif guess > random_number:
            print("too high")
    print("you guessed right")

predict(10)

def computer_guess(num):
    low=1
    high=num
    feedback=""
    while feedback!='C'and low!=high:
        guess = random.randint(low,high)
        feedback=input(f"is {guess}(H) high or too low(L) and if the guess is correct (C)")
        if feedback =='H':
            high=guess-1       
        elif feedback =='L':
            low=guess+1 
              
    print("computer guessed your number")
computer_guess(10)