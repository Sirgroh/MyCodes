rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random 

#0 rock, 1 paper, 2 scissor
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer = random.randint(0,3)

if user== 0 and computer==1:
    print(f"User Entered: Rock🪨 {rock}\n Coumputer Chose: Paper📜\n {paper}\n You Lose!")
elif user==0 and computer==2:
    print(f"User Entered: Rock🪨 {rock}\n Coumputer Chose: Scissor✂\n {scissors}\n You Win!")
elif user==1 and computer==0:
    print(f"User Entered: Paper📜 {paper}\n Coumputer Chose: Rock🪨\n {rock}\n You Win!")
elif user==1 and computer==2:
    print(f"User Entered: Paper📜 {paper}\n Coumputer Chose: Scissor✂\n {scissors}\n You Lose!")
elif user == 0 and computer ==0 :
    print(f"User Entered: Rock🪨 {rock}\n Coumputer Chose: Rock🪨\n {rock}\n It's a Tie!")
elif user == 1 and computer ==1 :
    print(f"User Entered: Paper📜 {paper}\n Coumputer Chose: Paper📜 {paper}\n It's a Tie!")
elif user == 2 and computer ==2 :
    print(f"User Entered: Scissor✂\n {scissors}\n Coumputer Chose: Scissor✂\n {scissors}\n It's a Tie!")
elif user==2 and computer==0:
    print(f"User Entered: Scissor✂\n {scissors}\n Coumputer Chose: Rock🪨\n {rock}\n You Lose!")
elif user==2 and computer==1:
    print(f"User Entered: Scissor✂\n {scissors}\n Coumputer Chose: Paper📜 {paper}\n You Win!")
else:
    pass