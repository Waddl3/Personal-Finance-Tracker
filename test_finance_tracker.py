from pathlib import Path
import json
from finance_tracker import greet_user 

def test_new_user_registration(tmp_path, monkeypatch, capsys):
    # Set up a temporary users.json file
    users_file = tmp_path / 'users.json'
    users_info = {}

    monkeypatch.setattr(Path, 'resolve', lambda x: users_file)

    # Mock user input
    monkeypatch.setattr('builtins.input', lambda x: 'John\nn')

    # Run the function
    greet_user()

    # Check the output
    captured = capsys.readouterr()
    assert 'Goodbye.' in captured.out

    # Check if the user is not added to the users_info dictionary
    assert not users_file.exists()
