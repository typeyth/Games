#RPSLS

import random 
while True:
    P1 = input("Rock, Paper, Scissors, Lizard, Spock: ")
    P2 = random.randint(1,5)

    if P2 == 1:
        P2 = "Rock"
    elif P2 == 2:
        P2 = "Paper"
    elif P2 == 3:
        P2 = "Scissors"
    elif P2 == 4:
        P2 = "Lizard"
    elif P2 == 5:
        P2 = "Spock"
        
    print(P2)

    if P1 == P2:
        print("Tie")
    elif (P1 == "Rock" and P2 == "Scissors") or (P1 == "Paper" and P2 == "Rock") or (P1 == "Scissors" and P2 == "Paper") or (P1 == "Rock" and P2 == "Lizard") or (P1 == "Paper" and P2 == "Spock") or (P1 == "Scissors" and P2 == "Lizard") or (P1 == "Spock" and P2 == "Scissors") or (P1 == "Spock" and P2 == "Rock") or (P1 == "Lizard" and P2 == "Spock") or (P1 == "Lizard" and P2 == "Paper"):
        print("Win")
    else:
        print("Loose")
    
    check = input("Restart: ")
    if check.upper() == "R":
       continue
    break