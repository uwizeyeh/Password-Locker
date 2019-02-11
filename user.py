class User:
    """
    Class that generates new instances of contacts.
    """

    user_list = [] # Empty contact list

    def __init__(self,first_name,last_name,user_name,password):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password
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
        self.new_user = User("yvette","umutesiwase","umutesiwaseyvette","yvette") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"yvette")
        self.assertEqual(self.new_user.last_name,"umutesiwase")
        self.assertEqual(self.new_user.user_name,"umutesiwaseyvette")
        self.assertEqual(self.new_user.password,"yvette")


if __name__ == '__main__':
    unittest.main()  



      










