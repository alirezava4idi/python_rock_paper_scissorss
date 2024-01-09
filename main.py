from random import randint

print("Winning rules of The Rock paper and scissor game is as follows: \n" +
      "rock vs paper->paper wins\n"+
      "rock vs scissors->rock wins\n"+
      "paper vs scissors->scissors wins", end="\n\n")

choices = {'1': "Rock", '2': "paper", '3': 'scissor'}

while True:
    print("Enter a choice:")
    print("1. Rock")
    print("2. paper")
    print("3. scissor", end="\n\n")

    print("User turn: ", end="")
    user_input = input()

    if user_input not in choices.keys():
        print("invalid input")
        continue
    else:
        user_choice = choices[user_input]
        print(f"User choice is {user_choice}", end="\n\n")
        print("Now its computer turn......", end="\n\n")

        computer_choice = choices[str(randint(1, 3))]
        print(f"computer choice is {computer_choice}")

        if user_choice == computer_choice:
            print(f"{user_choice} V/s {computer_choice}")

            print("it's a tie => no one wins")
        
        # rock vs paper
        elif user_choice == choices['1'] and computer_choice == choices['2']:
            print(f"Paper wins => Computer wins")
        elif user_choice == choices['2'] and computer_choice == choices['1']:
            print(f"Paper wins => User wins")
        
        # rock vs scissor
        elif user_choice == choices['1'] and computer_choice == choices['3']:
            print(f"Rock wins => User wins")
        elif user_choice == choices['3'] and computer_choice == choices['1']:
            print(f"Rock wins => Computer wins")
        
        # paper vs scissor
        elif user_choice == choices['2'] and computer_choice == choices['3']:
            print(f"Scissor wins => Computer wins")
        elif user_choice == choices['3'] and computer_choice == choices['2']:
            print(f"Scissor wins => User wins")
        
    
    print("\n")
    print("do you want to play again? (y/N)")
    ans = input()

    if ans.lower() != 'y':
        break