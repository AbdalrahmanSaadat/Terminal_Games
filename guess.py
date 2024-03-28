import random
# prompt for random number
def main():
    guess = 0
    pronun1 ="guess"
    pronun2 ="guesses"
    try:
        user_input = input("Type a number to be the maximum: ")
        the_number = random.randint(1, int(user_input))
        #print(the_number)
        the_number, guess = guessing_loop(the_number, guess)
        # print you got the correct number in {number} of guesses
        if guess != 1:
            print(f"You got it in {guess} {pronun2}")
        else:
            print(f"You got it in {guess} {pronun1}")
    except:
        print("Try to write a valid number!")
        quit()
    

def guessing_loop(number, guess):
    # prompt for guess
    #check if the guess under or below the number
    while True:
        user_guess = input("Make a guess: ")
        if user_guess.isdigit():
            user_guess = int(user_guess)
            if user_guess > number:
                print("You were above the number!")
                guess += 1

            elif user_guess < number:
                print("You were below the number!")
                guess += 1
            else:
                print("You got it!")
                guess += 1
                break
        else:
            print("write a valid number!")
            continue

    return number, guess


main()




