from instapy_cli import client
import os
import pickle

def new_dict(user, passwrd, path, caption):

    info_dict = {user: [passwrd, path, caption]}

def upload_dict(info_dict):
    with open('instagram.pickle', 'a') as db:
        db.write(info_dict)

def open_dict():
    with open('instagram.pickle', 'r') as db:
        for dict in db:
            print(dict)

#username : password, video path, caption

def main():
    print("Would you like to make a new account (1) or edit an existing account (2)?")
    choice = input("")
    if choice == "1":

        user = input("Username: ")
        passwrd = input("Password: ")
        path = input("Video path: ")
        caption = input("Caption: ")    

        
    
if __name__ == '__main__':
    main()