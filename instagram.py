from instapy_cli import client
import os
import pickle

def new_dict(user, passwrd, path, caption):
    info_dict = {user: [passwrd, path, caption]}
    return info_dict

def save_dict(info_dict):
    with open('instagram.pickle', 'ab') as dbfile:
        pickle.dump(info_dict, dbfile)

def edit_dicts(all_dicts):
    with open('instagram.pickle', 'wb') as dbfile:
        pickle.dump(all_dicts, dbfile)

def open_dict():
    if not os.path.exists('instagram.pickle'):
        return {}
    with open('instagram.pickle', 'rb') as dbfile:
        all_dicts = {}
        try:
            while True:
                all_dicts.update(pickle.load(dbfile))
        except EOFError:
            pass
    return all_dicts



def edit_account(db):
    user = input("Username to edit: ")
    if user in db:
        print(f"Current details: {db[user]}")
        passwrd = input("New Password (leave blank to keep current): ")
        path = input("New Path (leave blank to keep current): ")
        caption = input("New Caption (leave blank to keep current): ")

        if passwrd:
            db[user][0] = passwrd
        if path:
            db[user][1] = path
        if caption:
            db[user][2] = caption

        edit_dicts(db)
        print(f"Updated details: {db[user]}")
    else:
        print("Username not found.")


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
        save_dict(info_dict)
        open_dict()
    elif choice == "2":
        db = open_dict()
        edit_account(db)

    elif choice == "3":
        db = open_dict()
        for user, details in db.items():
            print(f"Username: {user}, Details: {details}")
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

        
    
if __name__ == '__main__':
    main()
    