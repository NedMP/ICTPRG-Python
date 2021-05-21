# Write a program called 'GetEmailAddress' that will keep asking the user until they enter a email address with a valid format. A Valid format of an email address in this case; contains an '@', at least 1 '.' and the domain name and account name is longer than 2 characters but not longer than 32 then print the Email Address as a string.

def GetEmailAddress(email):
    if "@" in email:
        accountName = email.split("@")[0]
        domainName = email.split("@")[1]

        if (len(accountName) > 2 and len(accountName) <= 32) and (len(domainName) > 2 and len(domainName) <=32) and ("." in domainName):
            return True
    return False

while True:
    email = input("Enter an email address: ")
    if GetEmailAddress(email): 
        print(email)
        break
    else:
        print("Not a valid email, please try again...")