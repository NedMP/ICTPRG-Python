# I HAVE NOT EDITED THIS YET, THIS IS MORE COMPLEX.

correctUser = input("PLEASE CHOOSE A USERNAME: ")
correctPass = input("PLEASE CHOOSE A PASSWORD: ")
checkPass = input("PLEASE REPEAT YOUR PASSWORD: ") 

if correctPass == checkPass:
    print("Welcome! Please continue to sign in!")

    while 1 == 1:

        print("================================")
        username = input("PLEASE ENTER YOUR USERNAME: ")
        password = input("PLEASE ENTER YOUR PASSWORD: ")
                
        if username == correctUser and password == correctPass:
            print("Thank you for signing in " + username)
            print("Have a nice day!")
            break
        else:
            print("Your username or password was incorrect. Please try again.")
            
else: 
    print("Your passwords did not match, please try again.")