# class User:
#     """
#     Class that generates new instances of contacts.
#     """

#     user_list = [] # Empty contact list

    # def __init__(self,first_name,last_name,user_name,password):

    #   # docstring removed for simplicity

    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.user_name = user_name
    #     self.password = password
global user_list 
class User:
	'''
	Class to create user accounts and save their information
	'''
	# Class Variables
	# global users_list
	user_list = []
	def __init__(self,first_name,last_name,password):
		'''
		Method to define the properties for each user object will hold.
		'''

		# instance variables
		self.first_name = first_name
		self.last_name = last_name
		self.password = password

	def save_user(self):
		'''
		Function to save a newly created user instance
		'''
		User.user_list.append(self)
		