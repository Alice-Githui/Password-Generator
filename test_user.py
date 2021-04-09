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

    def test_init(self):
        '''
        test that checks if our program instatiates as it should
        '''

        self.assertEqual(self.new_credentials.account_user_name, "githui")
        self.assertEqual(self.new_credentials.account_password, "1wergxvh")


if __name__ == "__main__":
    unittest.main()



