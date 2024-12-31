import data
import hashlib
def start():
    ans = input("Type L for login or type S if you are returning: ").lower()
    if ans == "l":
        user = input("Username: ")
        password = input("Password: ")
        check_user(user, password, data.database)
    elif ans == "s":
        user = input("Username: ")
        password = input("Password: ")
        email = input("Email: ")
        create_user(user, email, data.database, hash(password.encode('utf-8')).hexdigest())
    elif ans == 'print':
        print(data.database)
    else:
        start()

def add_to_dict(value, password, email,base):
    base[value] = [password, email] 

def create_user(username, email, database, password):
    if username in database:
        print("Sorry, username or email already exists, please try again!")
        start()
    else:
        add_to_dict(str(username), password, email, data.database)
        validated()

def check_user(username, password, database):
    if username in database:
        temp = database[username]
        if (hash(password.encode('utf-8')).hexdigest()) == temp[0]:
            validated()
        else: 
            print("Wrong password")
            start()
    else:
        print("username does not exist")
        start()

def hash(password):
    hashed_pass = hashlib.sha256(password)
    return hashed_pass

def validated():
    print("YIPPEEEEEEEEEE")
    start()
