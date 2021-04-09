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


class Credentials:
    '''
    class that generates an object of credentials
    '''
    cred_list = []

    def __init__(self, account_user_name, account_password):
        '''
        defines the properties of the credentials object
        '''
        self.account_user_name = account_user_name
        self.account_password = account_password

    def save_credentials(self):
        '''
        method to ensure that our credentials are being saved in the app
        '''
        Credentials.cred_list.append(self)

    
  
