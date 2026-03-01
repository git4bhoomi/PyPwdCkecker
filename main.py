import string
import getpass

def check_pwd():
    password = getpass.getpass("Enter the password:")
    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = wspace_count = special_count = 0
    
    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1 

        elif char in string.ascii_uppercase:
            upper_count += 1
        
        elif char in string.digits:
            num_count += 1
        
        elif char ==" ":
            wspace_count += 1

        else:
            special_count += 1

    if lower_count >=1:
        strength += 1
    if upper_count >=1:
        strength += 1
    if num_count >=1:
        strength += 1
    if wspace_count >=1:
        strength += 1
    if special_count >=1:
        strength += 1

    if strength ==1:
        remarks = "Very Bad"
    elif strength ==2:
        remarks = "Very Bad"
    elif strength ==3:
        remarks = "Weak password, consider changing"
    elif strength ==4:
        remarks = " Medium strength, could be better"
    elif strength ==5:
        remarks = "Strong Password"

    print("Your password has:")
    print(lower_count,"Lowercase characters")
    print(upper_count,"Uppercase characters")       
    print(num_count,"Numerical characters")
    print(wspace_count,"Whitespace characters")
    print(special_count,"Special characters")

    print("Password strength:", strength , remarks)

def ask_pwd(another_pwd=False):
    valid= False
    if another_pwd:
        choice=input("Do you want to enter another password(y/n):")
    else :
        choice=input("Do you want to check pwd(y/n):")

    while not valid:
        if choice.lower()=='y':
            return False
        elif choice.lower()=='n':
            return True
        else:
            print("Invalid,try again")


if __name__ == '__main__':
    print("Welcome to Password Strength Checker")
    ask_pw = ask_pwd()

    while not ask_pw:
        check_pwd()
        ask_pw = ask_pwd(True)



    
    
