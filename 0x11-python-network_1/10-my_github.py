#!/usr/bin/python3
import requests
import sys
"""
Python script that takes your GitHub credentials (username and password) and
uses the GitHub API to display your id
"""

if __name__ == '__main__':
    
    username = sys.argv[1]
    personal_access_token = sys.argv[2]
    url = f'https://api.github.com/users/{username}'
    headers = {'Authorization': f'token {personal_access_token}'}
    response = requests.get(url, headers=headers)
    print(response.json().get('id'))
