import unittest

from user import User 

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

if __name__ == "__main__":
    unittest.main()
