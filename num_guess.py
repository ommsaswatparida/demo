import random
i = random.randint(1,100)   #i is the number to guess

while True :
    try:
        choice = int(input("Guess the number between 1 and 100:"))
        
        if choice > i:
            print("Too high!")
        elif choice < i:
            print("Too low!")
        else:
            print("Congratulations! you guessed the number")
            break 
    
    except ValueError:
        print("Please enter a valid number")
