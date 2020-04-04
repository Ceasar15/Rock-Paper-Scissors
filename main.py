import time

print("*************************************")
print("*****made by Ceasar Agbekuadzi*******")
print("*************************************")

lose = "You lost this round"
win=("You won this round")
draw = ("There is a tie")
lives = 5
computer_lives=7
drew = 0
score =0
password_list=[]
while True:
    print("Please enter the following details")
    username=input("Please enter your Usernname  ")
    password=input("Please enter your password  ")
    searchfile = open("accounts.txt","r")
    for line in searchfile:
        password_list.append(line.strip())
        if username and password in password_list:
            print("Please wait, loading...")
            time.sleep(0.5)
            print("loading...")
            time.sleep(0.5)
            print("loading...")
            time.sleep(0.5)
            print("loading...")
            time.sleep(0.5)
            print("loading...")
            print("Access has been granted")
            print("ROCK ")
            print("PAPER")
            print("SCISSORS")
            print("THE RULES OF ROCK PAPER SCISSORS")
            print("Enter 'display lives ' to see remaining lives")
            print("Enter 'display score ' to see your score")
            print("Enter 'display draw ' to see draw")
            print("Enter 'exit' to end game")
            print('You start with', lives, "lives")
            print("Good Luck!")
            while True:
                rps = input('Rock,  Paper,  Scissors?   ')
                import random
                computer = ('rock', 'paper', 'scissors')
                computer = random.choice(computer)

                #ROCK IF STATEMENT
                if rps == 'rock' and computer == 'paper':
                    print("The computer chose ", computer)
                    print("**")
                    print("**")
                    print(lose)
                    print("**")
                    print("**")
                    lives -=1
                if rps == 'rock' and computer == 'scissors':
                    print("The computer chose ", computer)
                    print("**")
                    print("**")    
                    print(win)
                    print("**")
                    print("**")
                    score +=1
                if rps == 'rock' and computer == 'rock':
                    print("The computer chose ", computer)
                    print("**")
                    print("**")
                    print(draw)
                    print("**")
                    print("**")
                    drew +=1
                #Paper if Statement
                if rps == 'paper' and computer == 'rock':
                    print("The computer chose ", computer)
                    print("**")
                    print("**")
                    print(win)
                    computer_lives -=1
                    print("**")
                    print("**")
                    score +=1
                if rps == 'paper' and computer == 'scissors':
                    print("The computer chose ", computer)
                    print("**")
                    print("**")
                    print(lose)
                    print("**")
                    print("**")
                    lives -=1
                if rps == 'paper' and computer == 'paper':
                    print("The computer chose ", computer)
                    print("**")
                    print("**")
                    print(draw)
                    print("**")
                    print("**")
                    drew +=1
                #Scissors if Statement
                if rps == 'scissors' and computer == 'rock':
                    print("The computer chose ", computer)
                    print("**")
                    print("**")
                    print(lose)
                    print("**")
                    print("**")
                    lives -=1    
                if rps == 'scissors' and computer == 'paper':
                    print("The computer chose ", computer)
                    print("**")
                    print("**")
                    print(win)
                    computer_lives -=1
                    print("**")
                    print("**")
                    score +=1      
                if rps == 'scissors' and computer == 'scissors':
                    print("The computer chose ", computer)
                    print("**")
                    print("**")
                    print(draw)
                    print('**')
                    print('**')
                    drew +=1      
                if rps == 'display lives':
                    print(lives)
                if rps == "display score":
                    print(score)
                if rps == "display draw":
                    print(drew)            
                #LIVES
                if lives == 0:
                    print("Thanks for playing")
                    print("You have run out of lives")
                    print("You got ", score, " wins")
                    print("You drew", drew, " times")
                    stop = input("Press Enter to stop")
                    exit()
                if computer_lives == 0:
                    print("Thanks for playing")
                    print("The computer run out of its lives")
                    print("Your got ", score, " wins")
                    print("You drew", drew, " times")
                    stop = input("Press Enter to stop")
                    exit()
                if rps == "exit":
                    break
            else:
                print("Your password is incorrect")