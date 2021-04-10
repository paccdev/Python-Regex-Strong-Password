import pyperclip, re 

# # date = re.compile(r'(\d\d)-(\d\d)-(\d\d)')
# # mo = date.search("My birthday is on 02-01-91")
# # print("Birth date found:" + mo.group())
# # print("group 1:" + mo.group(1))

passwordrex = re.compile(r'''(
^(?=.*[A-Z].*[A-Z])
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




