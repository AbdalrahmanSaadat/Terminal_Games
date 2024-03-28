
def main():
    score = 0
    pronunciation1 = "point"
    pronunciation2 = "points"
    print("Welcome to my simple quiz!")
    while True:
        first = input("Do you want to play?(yes/no) ")
        optimized = first.lower()
        if optimized == "yes":
            print("Okay let's play!")
            score = questions(score)
            score_percent = (score / 4 )* 100
            if score == 1:
                print(f"You got {score} {pronunciation1}!")
            else:
                print(f"You got {score} {pronunciation2}!")
            print(f"Your perentage is {score_percent}%")
            break
        elif optimized == "no":
            print("Good Bye")
            quit()
        else:
            print("Try again!")
            continue

    
    
def questions(score):
    
    q1 = input("what does CPU stands for?\n")
    if q1.lower() == "central processing unit":
        print("correct!")
        score += 1
    else:
        print("Incorrect!")
    
    q2 = input("what does GPU stands for?\n")
    if q2.lower() == "graphics processing unit":
        print("correct!")
        score += 1
    else:
        print("Incorrect!")

    q3 = input("what does RAM stands for?\n")
    if q3.lower() == "random access memory":
        print("correct!")
        score += 1
    else:
        print("Incorrect!")

    q4 = input("what does PSU stands for?\n")
    if q4.lower() == "power supply":
        print("correct!")
        score += 1
    else:
        print("Incorrect!")
    return score
    
main()