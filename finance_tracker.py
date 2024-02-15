from pathlib import Path
import json

if __name__ == "__main__":
    # Main block
    
    # empty dictionary for storing username and password
    usernames = {}
    path = Path('usernames.json')   # Storing data
    usernames = path.read_text()    # Retrieving data
    
    print("Welcome to your Personal Finances!")
    user = input('Please enter username: ')
    if user in usernames:
        print(f'Welcome back {user}!')
        while True:
            password = input('\nPlease enter password: ')
            if password == usernames[user]:
                print(f'You are now logged in {user}!')
                break
            else:
                print('Inorrect Password, please try again')
    else:
        new_user = input(f'\n{user} was not found. 
                         "Would you like to register a new account? (y/n) ').lower()
        if new_user == 'y':
            password = input('Please enter a password: ')
            usernames[user] = password
            print(f'Username {user} has been successfully created!')
    
    
    