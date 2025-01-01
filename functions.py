import data
import hashlib
def start():
    ans = input("Type L for login or type S if you are returning: ").lower()
    if ans == "l":
        user = input("Username: ").replace(" ", "")
        password = input("Password: ").replace(" ", "")
        data.read_data(data.cursor,user,password)
    elif ans == "s":
        user = input("Username: ").replace(" ", "")
        password = input("Password: ").replace(" ", "")
        email = input("Email: ").replace(" ", "")
        data.add_data(data.cursor,user,password, email)
    elif ans == 'print':
        print(data.database)
        data.contents(data.database, data.cursor)
        data.wipe()
        print("Database wiped")
    else:
        start()

def hash(password):
    hashed_pass = hashlib.sha256(password)
    return hashed_pass

def validated():
    print("SECRET MESSAGE")
    start()

