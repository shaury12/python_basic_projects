import random
options = ["snake", "water","gun"]

print("WELCOME , to the ultimate snake, water and gun game.")
print("Kindly enter your name,")
print("..", end  ="")
name = input()


print(f"Hello {name}, let's begin the game")
print("There will be 5 rounds between you and the computer")
print("Whoever wins the most rounds wins the game")

players_win = 0
computers_win = 0
running = True

while running:
    for i in range(1,6):
        print()
        print(f"ROUND {i}")

        players_choice = input("Choose snake, water or gun: ")
        computers_choice = random.choice(options)
        if players_choice.lower() == options[0]:
            if computers_choice == options[1]:
                print(f"{name}, you win and Computer loses.")
                players_win +=1
            elif computers_choice == options[2]:
                print(f"{name}, you lose and Computer wins.")
                computers_win+=1
            else:
                print(f"It's a tie")
        elif players_choice.lower() == options[1]:
            if computers_choice == options[2]:
                print(f"{name}, you win and Computer loses.")
                players_win +=1
            elif computers_choice == options[0]:
                print(f"{name}, you lose and Computer wins.")
                computers_win+=1
            else:
                print(f"It's a tie")
        elif players_choice.lower() == options[2]:
            if computers_choice == options[0]:
                print(f"{name}, you win and Computer loses.")
                players_win +=1
            elif computers_choice == options[1]:
                print(f"{name}, you lose and Computer wins.")
                computers_win+=1
            else:
                print(f"It's a tie")
        else:
            print("Wrong input! ERROR")
            break
        print(f"You chose {players_choice} and computer chose {computers_choice}.")
        print()
        print(f"{name}'s rounds won: {players_win}")
        print(f"Computer's rounds won: {computers_win}")
        print()
        print(f"End of round {i}.")
        print()
    if players_win > computers_win:
        print(f"Congratulations {name}, you win by {players_win - computers_win} rounds.")
    elif computers_win> players_win:
        print(f"{name}, you lose by {computers_win-players_win} rounds.")
    else:
        print(f"It's a tie, nice game.")

    print()
    print("Would you like to restart the game? Y/n")
    continue_game = input()

    if continue_game == "n" or continue_game == "N":
        running = False
    else:
        pass

print("Thanks for playing our game.")

    
