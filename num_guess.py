import random
while True :
    choice = int(input("Guess the number between 1 and 100:"))
    i = random.randint(1,100)
    if choice == i :
        print("Congratulations! You guessed the number")
    elif choice >> i:
        print("Too high!")
    elif choice << i:
        print("Too low!")
        break 
    else:
        print("Please enter a valid number")

