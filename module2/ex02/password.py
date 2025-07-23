import getpass

password = "pass123"

pwd  = getpass.getpass("Password:")

if pwd == password:
    print("ACCESS GRANTED")
else :
    print("ACCESS DENIED")