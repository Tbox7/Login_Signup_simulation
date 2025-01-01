import sqlite3
import functions
import os
database = sqlite3.connect('entries.db')
cursor = database.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS credentials
               (Username TEXT,
               Password TEXT,
               Email TEXT)
               ''')
database.commit()
###Checks to see if username exists if not appends(username, password, email)
def add_data(cursor,username, password, email):
    cursor.execute('SELECT * FROM credentials WHERE username = ?', (username,))
    found = cursor.fetchone()
    if found:
        print("Sorry, this username already exists, please try again")
        functions.start()
    else:
        hashed_password = functions.hash(password.encode('utf-8')).hexdigest()
        cursor.execute('''
        INSERT INTO credentials (Username, Password, Email) VALUES (?,?,?)
        ''', (username, hashed_password, email))
        database.commit()
        functions.validated()
###Checks to see if the username and password exist within the database
def read_data(cursor,username,password):
    if cursor.execute('SELECT * FROM credentials WHERE Username = ?', (username,)):
        found = cursor.fetchone()
        hashed_password = functions.hash(password.encode('utf-8')).hexdigest()
        if found:
            stored_password = found[1]  
            if hashed_password == stored_password: 
                functions.validated() 
            else: 
                print("Sorry, wrong password, please try again") 
                functions.start() 
        else: 
            print("Sorry, wrong username, please try again")
            functions.start()
    else:
        print("Sorry wrong username, please try again")
        functions.start()
###Prints all the contents of the table in the terminal
def contents(database, cursor):
    cursor.execute('SELECT * From credentials')
    rows = cursor.fetchall()
    column_names = [description[0] for description in cursor.description] 
    print(column_names)
    for row in rows:
        print(row) 
        print()
    database.close()
###Wipes tables and restarts program
def wipe():
    os.remove('entries.db')
