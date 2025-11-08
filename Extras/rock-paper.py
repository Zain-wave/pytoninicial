import random

def play():
    options =["rock", "paper", "scissors"] 
    user = str(input("Select rock, paper or scissors ")).lower()
    computer = random.choice(options)
    
    if user not in options:
        print("❌ Select a valid option")
        return
    
    print(f"\n You selected {user}")
    print(f"\n Computer selected {computer}")
    
    if computer == user:
        print("Draw")
    elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
        print("Ganaste")
    else:
        print("Perdiste")


play()