from instapy_cli import client
import os
import pickle
from instagrapi import Client

class AccountManagement:            
    def new_dict(self, user, passwrd, path, caption):
        info_dict = {user: [passwrd, path, caption]}
        return info_dict

    def save_dict(self, info_dict):
        with open('instagram.pickle', 'ab') as dbfile:
            pickle.dump(info_dict, dbfile)

    def edit_dicts(self, all_dicts):
        with open('instagram.pickle', 'wb') as dbfile:
            pickle.dump(all_dicts, dbfile)

    def open_dict(self):
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

    

    def edit_account(self, db):
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

            self.edit_dicts(db)
            print(f"Updated details: {db[user]}")
        else:
            print("Username not found.")

    def main(self):
        print("Would you like to make a new account (1) or edit an existing account (2)?")
        choice = input("")
        if choice == "1":

            user = input("Username: ")
            passwrd = input("Password: ")
            path = input("Video path: ")
            caption = input("Caption: ")    

            info_dict = self.new_dict(user, passwrd, path, caption)
            self.save_dict(info_dict)
            self.open_dict()
        elif choice == "2":
            db = self.open_dict()
            self.edit_account(db)

        elif choice == "3":
            db = self.open_dict()
            for user, details in db.items():
                print(f"Username: {user}, Details: {details}")
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

            
        

if __name__ == '__main__':
    account_manager = AccountManagement()
    #account_manager.main()


cl = Client()


dict_list = account_manager.open_dict()

user_list = list(dict_list.keys())
values_list = list(dict_list.values())
pass_list = []
path_list = []
caption_list = []
for i in values_list:
    pass_list.append(i[0])
    path_list.append(i[1])
    caption_list.append(i[2])



cl.login(user_list[0], pass_list[0])
cl.clip_upload(path_list[0], caption_list[0])
