def register():
    email = input("Enter email_id: ")
    password = input("Enter password: ")
    for line in open("loginpwd.txt","r").readlines(): # Read the lines
        login_info = line.split() # Split on the space, and store the results in a list of two strings
        if email == login_info[0]:
            print("User already registered")
            login()
            return True
    print("New user")
    file = open("loginpwd.txt","a")
    file.write(email)
    file.write(" ")
    file.write(password)
    file.write("\n")
    file.close()
    return False
def login():
    email = input("Enter email_id: ")
    password = input("Enter password: ")
    for line in open("loginpwd.txt","r").readlines(): # Read the lines
        login_info = line.split() # Split on the space, and store the results in a list of two strings
        if email == login_info[0] and password == login_info[1]:
            print("Correct credentials!")
            return True
    print("Incorrect credentials.")
    return False

def forgetpwd():
    email = input("Enter email: " )
    for line in open("loginpwd.txt","r").readlines(): # Read the lines
        login_info = line.split() # Split on the space, and store the results in a list of two strings
        if email == login_info[0]:
            print("Original password is", login_info[1])
            return True
        else:
            print("No matches found start register again")
            register()
            return False