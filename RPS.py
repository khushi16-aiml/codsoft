import random 
user_wins = 0
comp_wins = 0
option = ["rock","paper","scissor"]

while True:
    user_ans = input("Choose rock/paper/scissor or Q to quit")
    if user_ans == "Q":
        break
    if user_ans not in option:
        print("Please choose a valid option")
        continue
    computer_choose = random.choice(option)
    print(f"Computer choose {computer_choose}.")
    if user_ans == computer_choose:
        print("Tie")
    elif user_ans == "rock" and computer_choose == "scissor":
        print("you win!")
        user_wins+=1
    elif user_ans == "paper" and computer_choose == "rock":
        print("you win!")
        user_wins+=1
    elif user_ans == "scissor" and computer_choose == "paper":
        print("you win")
        user_wins+=1
    else:
        print("you lost!")
        comp_wins+=1
print("See you next time, Goodbye")   