import random
n = random.randint(1,100)
a = -1
guesses = 1
print("Welcome to perfect guess game!")
while(a!=n):
    a = int(input("Guess the number(within 100):"))
    if(a>n):
        print("Guess Lower Number please!")
        guesses +=1
    elif(a<n):
        print("Guess Higher Number please!")
        guesses +=1
print(f"You have guessed the number {n} correctly in {guesses} attempts.")
print("Thank you for playing perfect guess game!")