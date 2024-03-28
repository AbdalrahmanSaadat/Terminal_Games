import random


def main():
    pl_score = 0
    comp_score = 0
    pl_score, comp_score = playing(pl_score,comp_score)
    print(f"You won {pl_score} times")
    print(f"Computer won {comp_score} times")
    print("Good bye!")

def computer_choice():
    choices = ["rock", "paper", "scissors"]
    r_choice = random.randint(0,2)
    the_choice = choices[r_choice]
    return the_choice


def playing(p_score, c_score):
    p_score = 0
    c_score = 0
    while True:
        user = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
        comp = computer_choice()
        if user == "q":
            break

        elif user == comp:
            print(f"Computer picked {comp}")
            print("Draw!")
            continue

        elif user == "rock" and comp =="scissors":
            print(f"Computer picked {comp}")
            print("You win!")
            p_score += 1
            continue

        elif user == "scissors" and comp == "paper":
            print(f"Computer picked {comp}")
            print("You win!")
            p_score += 1
            continue
        
        elif user == "paper" and comp == "rock":
            print(f"Computer picked {comp}")
            print("You win!")
            p_score += 1
            continue
        else:
            print(f"Computer picked {comp}")
            print("You lost!")
            c_score += 1
            continue
        
    return p_score, c_score

main()