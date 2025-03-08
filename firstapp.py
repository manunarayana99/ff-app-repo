import getpass
actual_word=getpass.getpass()
guess_word=input("enter your word")
if actual_word==guess_word:
    print("mathched")
else:
    print("unmatched")
    