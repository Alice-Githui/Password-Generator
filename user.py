import random 
import pyperclip

class User:
    '''
    class that generates an object of user
    '''

    user_list = [] #create a list where all our users are saved

    def __init__(self, username, password):
        '''
        defines the properties of our users

        Args:
        self.username = username
        self.password = password
        '''
        self.username = username
        self.password = password

    def save_user(self):
        '''
        method to ensure that our user objects are being saved in the app
        '''
        User.user_list.append(self)


class Credentials:
    '''
    class that generates an object of credentials
    '''
    cred_list = []

    def __init__(self, account_type, account_user_name, account_password):
        '''
        defines the properties of the credentials object
        '''
        self.account_type = account_type
        self.account_user_name = account_user_name
        self.account_password = account_password

    def save_credentials(self):
        '''
        method to ensure that our credentials are being saved in the app
        '''
        Credentials.cred_list.append(self)

    def delete_credentials(self):
        '''
        method/attribute to delete a credential object that is no longer in use
        '''
        Credentials.cred_list.remove(self)
    
    @classmethod
    def find_credentials(cls, account_type):
        '''
        method that checks if an account exists and returns that account
        '''
        for credentials in cls.cred_list:
            if credentials.account_type == account_type:
                return credentials
    
    @classmethod
    def display_credentials(cls):
        '''
        method to display all the credentials in the cred_list list
        '''
        return cls.cred_list

    @classmethod
    def credentials_exist(cls, account_type):
        '''
        method that checks if credentials exists using a account-name. Returns a boolean

        Args:
        account-type to search for
        '''
        for credentials in cls.cred_list:
            if credentials.account_type == account_type:
                return True

        return False              
    
    def generate_password():
        password = ""
        for i in range(8):
            i = chr(random.randint(65,90))
            j = chr(random.randint(65,90)).lower()
            k = random.randint(0,9)
            password = str(password) + i + j +str(k)

        print(password)



    
  
