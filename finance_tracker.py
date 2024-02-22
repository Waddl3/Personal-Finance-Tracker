from pathlib import Path
import json

def valid_password(users_info, user):
    print(f'Welcome back {user}!')
    password = input('Please enter your password: ')
    if password == users_info[user]:
        print(f'You are now logged in {user}!')
    else:
        print('Incorrect: Password Does not match.')

def register_new_user(users_info, user, path):
    user_choice = input('No user found. Would you like to register? (y/n) ').lower()
    if user_choice == 'y':
        password = input('Please register a password: ')
        users_info[user] = password
        contents = json.dumps(users_info)
        path.write_text(contents)
        print(f'Username {user} has successfully been created!')
    else:
        print('Goodbye.')
    return users_info
        
def load_user_data(path):
    if path.exists():
        return json.loads(path.read_text())
    return {}

def greet_user():
    '''Greet the user by name.'''
    
    path = Path('users.json')
    users_info = load_user_data(path)
    
    # Intro
    print('Personal Fianance Tracker')
    
    user = input('Please enter your username: ')
    if user in users_info:
        valid_password(users_info, user)
    else:
        users_info = register_new_user(users_info, user, path)
    
        
if __name__ == "__main__":
    # Main block
    greet_user()
    
            