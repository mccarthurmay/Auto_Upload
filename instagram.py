from instapy_cli import client
import os
import pickle

def new_dict(user, passwrd, path, caption):
    info_dict = {user: [passwrd, path, caption]}
    return info_dict

def upload_dict(info_dict):
    with open('instagram.pickle', 'ab') as db:
        pickle.dump(info_dict, db)


def open_dict():
    with open('instagram.pickle', 'rb') as db:
        print(pickle.load(db))

#username : password, video path, caption

def main():
    print("Would you like to make a new account (1) or edit an existing account (2)?")
    choice = input("")
    if choice == "1":

        user = input("Username: ")
        passwrd = input("Password: ")
        path = input("Video path: ")
        caption = input("Caption: ")    

        info_dict = new_dict(user, passwrd, path, caption)
        upload_dict(info_dict)
        open_dict()

        
    
if __name__ == '__main__':
    main()
    