import unittest # Importing the unittest module
from user import User # Importing the user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the User class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    ''' 
     # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Hulde","Uwizeyimana","huldeuwizeyimana@gmail.com","hulde") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Hulde")
        self.assertEqual(self.new_user.last_name,"Uwizeyimana")
        self.assertEqual(self.new_user.user_name,"huldeuwizeyimana@gmail.com")
        self.assertEqual(self.new_user.password,"hulde")


    def test_save_user(self):
        '''
        test_save_account test case to test if the account object is saved into
         the account list
        '''
        self.new_user.save_user() # saving the new account
        self.assertEqual(len(User.user_list),1)

    # Items up here...

    def test_save_multiple_user(self):
            '''
            test_save_multiple_account to check if we can save multiple account
            objects to our account_list
            '''
            self.new_user.save_user()
            test_user = User("Hulde","Uwizeyimana","huldeuwizeyimana@gmail.com","hulde") # new account
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)

    #setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

    # other test cases here
    def test_save_multiple_user(self):
            '''
            test_save_multiple_account to check if we can save multiple account
            objects to our account_list
            '''
            self.new_user.save_user()
            test_user = User("Hulde","Uwizeyimana","huldeuwizeyimana@gmail.com","hulde") # new account
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)    


if __name__ == '__main__':
    unittest.main()  
