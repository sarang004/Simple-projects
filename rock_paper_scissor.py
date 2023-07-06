import random
user_wins=0
comp_wins=0
options=['rock','paper','scissor']
while True:
    user_input=input("Type Rock/Paper/Scissor or Q to quit: ").lower()
    if user_input == 'q' :
        print("Player Score : ",user_wins)
        print("Computer Score : ",comp_wins)
        break
    if user_input not in options:
        print("Enter the correct option : ")
        continue
    rand_num = random.randint(0,2)
    comp_pick=options[rand_num]
    print("Computer Picked :",comp_pick)
    if(user_input=='scissor' and comp_pick=='paper'):
        print("User Wins")
        user_wins=user_wins+1
    elif(user_input=='rock' and comp_pick=='scissor'):
        print("User wins")
        user_wins+=1
    elif(user_input=='paper' and comp_pick=='rock'):
        print("User wins")
        user_wins+=1
    elif(user_input==comp_pick):
        print("No One WIns")
    else:
        print("Computer wins")
        comp_wins+=1
