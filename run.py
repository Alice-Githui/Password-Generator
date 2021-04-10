#!/usr/bin/env python3.9

from user import User
from user import Credentials

def create_user(username, password):
    '''
    Function to create a new user
    '''
    new_user = User(username, password)
    return new_user

def save_new_user(user):
    '''
    Function that saves new users
    '''
    user.save_user()

def create_credentials(account, account_username, acc_password):
    '''
    Function that creates new account credentials
    '''
    new_credentials = Credentials(account, account_username, acc_password)
    return new_credentials

def save_credentials(credentials):
    '''
    Function that saves new credentials that are generates
    '''
    credentials.save_credentials()

def delete_credentials(credentials):
    '''
    Function that deletes the credentials that are no longer being used
    '''
    credentials.delete_credentials()

def find_credentials(account_type):
    '''
    Function that returns a credential if it exists in the cred_list 
    '''
    return Credentials.find_credentials(account_type)

def if_credentials_exist(account_type):
    '''
    Funstion that checks if a contact exists in the cred_list list
    '''
    return Credentials.credentials_exist(account_type)

def display_all_credentials():
    '''
    Function that displays all the contacts that are saved in the cred_list
    '''
    return Credentials.display_credentials()

def generate_random_password():
    '''
    Function that generates a random password for the user
    '''
    auto_password = Credentials.generate_password()
    return auto_password

def main():
    print("Password Locker App")
    user_name = input("Enter your username: ")

    print(f"Hello {user_name}. What would you like to do?")
    print("\n")

    while True:
        print("Use these short-codes: cu - create user, lg - login into the account")

        short_code = input().lower()

        if short_code == "cu":
            print("New User")
            print("-" *20)

            print("Enter preferred username")
            username = input()

            print("Enter preferred password")
            password = input()

            print("Confirm password")
            confirm_password = input()


            while confirm_password != password:
                print("Passwords do not match")
                print("Enter your password:")
                password = input()
                print("Confirm your password")
                confirm_password = input()
            else: 
                print(f"Account successfully created. {username} welcome to your password locker account")
                print(f"New User: {username} created")
                print("Proceed to login:")
                print("Enter your username")
                entered_username = input()
                print("Enter your password")
                entered_password = input()
            
            while entered_username != username or entered_password != password:
                print("Account details do not match")
                print("Please confirm your account details")
                print("Username")
                entered_username = input()
                print("Password")
                entered_password = input()

            else:
                print(f"{username} Welcome to Password Locker!!")
                print("*" *40)        
        
        elif short_code == "lg":
            print("Login into your account")
            print("Enter your username:")
            login_username = input()
            print("Enter your password")
            login_password = input()

            print(f"{login_username}. You have successfully logged in to your account") 

        while True:
            print("Use these short codes to proceed: cc - create new credentials, dl- delete credentials, dc - display credentials, ex - exit the app")

            short_code = input().lower().strip()

            if short_code == "cc":
                print("Create new account credentials: .... ")
                print("-" *30)
                print("Which app are you creating a password?")
                account = input()
                print("Enter the preferred username:")
                account_username =  input()

                while True:
                    print("Use these to generate a password: op - own password, gp - generated password")

                    password_Type = input().lower().strip()

                    if password_Type == "gp":
                        password = generate_random_password()
                        break
                    elif password_Type == "op":
                        print("Enter a password")
                        password = input()
                        break
                    else: 
                        print("Choose either of the above")
                save_credentials(create_credentials(account, account_username, password))

                print("\n")
                print(f"Account for {account}, username {account_username} created successfully")
            
            elif short_code == "dl":
                print("Enter the account for the credentials you want to delete")
                search_account = input().strip()
                if find_credentials(search_account):
                    search_credentials = find_credentials(search_account)
                    search_credentials.delete_credentials()

                    print("\n")
                    print(f"Your {search_account} credentials have been successfully deleted!!!")
                else:
                    print(f"The credentials you are looking for cannot be found.")



                    




        # elif short_code =="ex":
        #     break   

        # else:
        #     print("I didn't get that. Kindly use short codes")       



if __name__ =="__main__":
    main()





