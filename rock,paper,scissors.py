import random

while True:
    choices = ("rock 🪨","paper 📃","scissors ✂️")
    a = random.choice(choices)
    try:
        choice = input("Rock, Paper or Scissors? (r/p/s):").lower()
        key = {"r":"rock 🪨","p":"paper 📃","s":"scissors ✂️"}
        
        if choice == "q":
            print("Thanks for playing!")
            break
        
        print("you chose " , key[choice])       
        print("the computer chose", a)
        
        if choice == "r":
            if a == "rock 🪨":
                print("it's a tie")
            elif a == "scissors ✂️":
                print("you win")
            else:
                print("you lose")
        
        elif choice == "p":
            if a == "paper 📃":
                print("it's a tie")
            elif a == "rock 🪨":
                print("you win")
            else:
                print("you lose")
        
        else: 
            if a == "scissors ✂️":
                print("it's a tie")
            elif a == "paper 📃":
                print("you win")
            else:
                print("you lose")
            
    except KeyError:
        print("Please enter a valid input" )
    
        

    
     
    


    