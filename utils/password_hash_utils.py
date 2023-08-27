"""
password_hash_utils.py - A utility script for generating hashed passwords using
streamlit-authenticator.

This script prompts the user to enter passwords to hash using the `Hasher` class
in `streamlit-authenticator`. The hashed passwords are printed to the console
for the user to copy and paste into a `config.yaml` file.

Usage:
    $ python password_hash_utils.py
"""

import streamlit_authenticator as stauth

# User instructions
print("You will be prompted to enter passwords to hash. Enter an empty string to exit.")
password = input('Enter password: ')

while password != '':
    hashed_password = stauth.Hasher([password]).generate()
    print(f'Hashed password: {hashed_password}')
    password = input('Enter next password: ')

print('Exiting...')
