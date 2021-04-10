# Python-Regex-Strong-Password
import pyperclip, re 


passwordrex = re.compile(r'''(
^(?=.*[A-Z].*[A-Z])
(?=.*[a-z].*[a-z])
(?=.*[0-9].*[0-9])
(?=.*[!@$&*])
)''', re.VERBOSE)

def userinput():
    print("please input a password")
    choice = str(input())
    validation = passwordrex.search(choice)
    if not validation:
        print("password is not enough")
    else:
        print(validation)
