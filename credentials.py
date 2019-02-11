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
# Items up here...

    def test_save_multiple_user(self):
            '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
            '''
            self.new_user.save_user()
            test_user = User("Test","first_name","last_name","user_name","password") # new contact
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)

if __name__ == '__main__':
    unittest.main()
