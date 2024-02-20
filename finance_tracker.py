from pathlib import Path
import json

def greet_user():
    '''Greet the user by name.'''
    # empty dictionary
    users_info = {}
    
    path = Path('users.json')
    if path.exists():
        contents = path.read_text()
        users_info = json.loads(contents)
    
    # Intro
    print('Personal Fianance Tracker')
    
    user = input('Please enter your username: ')
    if user in users_info:
        print(f'Welcome back {user}!')
        password = input('Please enter your password: ')
        
        if password == users_info[user]:
            print(f'You are now logged in {user}!')
        else:
            print('Incorrect: Password Does not match.')
    else:
        new_user = input('No user found. Would you like to register? (y/n) ').lower()
        if new_user == 'y':
            password = input('Please register a password: ')
            users_info[user] = password
            contents = json.dumps(users_info)
            path.write_text(contents)
            print(f'Username {user} has successfully been created!')
        else:
            print('Goodbye.')
    
        
if __name__ == "__main__":
    # Main block
    greet_user()
    
            