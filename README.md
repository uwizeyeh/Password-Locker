# Project
Password Locker
# Author
Uwizeyimana Hulde

## Description
This is a python terminal application that allows a user to generate and store passwords for various accounts.


## Setup/Installation Requirements
To start using this project use the following commands:

* git clone https://github.com/uwizeyeh/Password-Locker
* cd Password-Locker
To run this program

* run this command lines in your terminal:
* chmod +x run.py
* ./run.py
## Behavior Driven Development
The program should ask for user's username and password when ca(create account) is entered:

  * Input Example: Enter ca

  * Output Example: What is your username?

  * Output Example: What is your password?

The program should authenticate the account by asking the user to login again when cc(create credential) is entered:

  * Input Example: Enter cc

  * Output Example: Login to your account. Username?

The program should create credentials when cc(create credential) is entered:

  * Input Example: Enter cc

  * Output Example: Enter the account name

The program should generate a random 8 characters long password when gp(generate password) is   entered:

  * Input Example: Enter gp

  * Output Example: Your password is:

The program should let the user create their own password when cp(create password) is entered:

   * Input Example: Enter cp

   * Output Example: Enter your password

The program should display the credentials when dc(display credentials) is entered:

   * Input Example: Enter dc

   * Output Example: Here is a list of all of your credentials...

The program should end when ex(exit program) is entered:

   * Input Example: Enter ex

   * Output Example: Thank you for using Password locker...

## License
MIT License

Copyright (c) 2019 