import random

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

rps_images = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_choice = random.randint(0, 2)

print(rps_images[choice])
print(f"Computer chose:\n{rps_images[computer_choice]}")

if choice == 0 and computer_choice == 2:
    print("You win")
elif choice == 1 and computer_choice == 0:
    print("You win")
elif choice == 2 and computer_choice == 1:
    print("You win")
elif choice == 0 and computer_choice == 1:
    print("You lose")
elif choice == 1 and computer_choice == 2:
    print("You lose")
elif choice == 2 and computer_choice == 0:
    print("You lose")
else:
    print("Tie")