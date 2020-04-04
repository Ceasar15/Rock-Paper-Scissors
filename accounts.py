print("*************************************")
print("ROCK, PAPER, SCISSORS Account setup")
print("*************************************")

while True:
        username = input("Please choose your username  ")
        password = input("Please choose your password  ")
        password_confirm = input("Please confirm your password  ")
        if password != password_confirm:
            print("Your passwords do not match. Please try again")
        if password == password_confirm:
            print("Your account has been setup")
        text_file = open("accounts.txt", "a")
        text_file.write('\n')
        text_file.write(username)
        text_file.write('\n')
        text_file.write(password)
        text_file.close()
        break



        



