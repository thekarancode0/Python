import random

def checkWin(you ,computer):
    if(you!="" or computer!=""):
        if(you=='s' and computer=='p'):
            return 1
        elif(you=='p' and computer=='r'):
            return 1
        elif(you=='r' and computer=='s'):
            return 1
        elif(you=='s' and computer=='r'):
            return 0
        elif(you=='p' and computer=='s'):
            return 0
        elif(you=='r' and computer=='p'):
            return 0
        elif(you=='s' and computer=='s'):
            return 2
        elif(you=='p' and computer=='p'):
            return 2
        elif(you=='r' and computer=='r'):
            return 2
        else:
            print("Invalid")

        

#user choice
            
for i in range(1,20):
    print("*****Rock Paper Scissors*****")
    you=(input("Enter you choioce\ns for Scissor\np for Paper\nr for Rock--->"))
    print(you)

    option=['s','p','r','r','p','s']
    computer=random.choice(option)
    print("computer--->",computer)

    result=checkWin(you,computer)
    if(result==1):
        print("You win\3")
    elif(result==0):
        print("you loose!!")
    elif(result==2):
        print("Game Draw!!!")
    else:
        print("Invalid")
    print("\n")
