import unittest


from user import User 
from user import Credentials

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for our user object

    Args:
    unittest:TestCase - TestCase class that helps in defining test cases
    '''

    #test to confirm that our object is instatiated properly
    def setUp(self):
        '''
        setUp method to define the properties of the user
        '''
        self.new_user = User("alice", "qwerty")

    def test_init(self):
        '''
        test to confirm that the user object instatiates properly
        '''
        self.assertEqual(self.new_user.username, "alice")
        self.assertEqual(self.new_user.password, "qwerty")


class TestCredentials(unittest.TestCase):
    '''
    Test that defines test cases for our objets
    '''

    def setUp(self):
        '''
        set up method that determines the properties of the credentials object
        '''
        self.new_credentials = Credentials("githui", "1wergxvh")

    def tearDown(self):
        '''
        tearDown method that runs every time our app runs. It is implemented when checking if multiple credential objects are being savd in our app

        Args:
        create an empty credentials list (cred_list)
        '''
        Credentials.cred_list = []

    def test_init(self):
        '''
        test that checks if our program instatiates as it should
        '''

        self.assertEqual(self.new_credentials.account_user_name, "githui")
        self.assertEqual(self.new_credentials.account_password, "1wergxvh")
    
    def test_save_credentials(self):
        '''
        test to determine if our generated credentials are being saved in the app
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.cred_list), 1)

    def test_save_multiple_credentials(self):
        '''
        test to check if our app saves multiple credentials created in the cred_list list
        '''
        self.new_credentials = Credentials("two", "deux2")
        self.new_credentials.save_credentials()
        test_credentials = Credentials("trois", "trois3")
        test_credentials.save_credentials()

        self.assertEqual(len(Credentials.cred_list), 2)

    def test_delete_credentials(self):
        '''
        test that checks if we can delete a credential object that is no longer being used
        '''
        self.new_credentials = Credentials("two", "deux2")
        self.new_credentials.save_credentials()
        test_credentials = Credentials("trois", "trois3")
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.cred_list), 1)


if __name__ == "__main__":
    unittest.main()



