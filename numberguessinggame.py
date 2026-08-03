import random

secret = random.randint(1, 100)
print(secret)

def num():
    return int(input("Enter your guess: "))
    
attempts = 0

guess = num()

while guess != secret:
    if(guess < secret):
        print("your number is smaller ! ")
        guess = num()
        
    elif(guess > secret):
        print("Your number is bigger!")
        guess = num()
        
    attempts += 1    

else:
    print("You matcheed your number !")
    print(f"you matched it in {attempts} attempts")