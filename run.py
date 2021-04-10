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

def create_credentials(credentials):
    '''
    Function that creates new account credentials
    '''
    credentials.create_new_credentials()

def save_credentials(credentials):
    '''
    Function that saves new credentials that are generates
    '''
    credentials.save_new_credentials()

def delete_credentials(credentials):
    '''
    Function that deletes the credentials that are no longer being used
    '''
    credentials.delete_credentials()

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
    print("/n")

    while True:
        print("Use these short-codes: cu - create user, lg - login into the account, ex-exit the system")

        short_code = input().lower()

        if short_code == "cu":
            print("New User")
            print("-" * 20)

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
                print("/n")
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
                username = input()
                print("Password")
                password = input()

            else:
                print(f"{username} Welcome to Password Locker!!")
                print("-" * 20)        
        
        elif short_code == "lg":
            print("Login into your account")
            print



if __name__ =="__main__":
    main()





