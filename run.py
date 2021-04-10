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

def main():
    print("Welcome to the Password Locker App")


if __name__ =="__main__":
    main()





