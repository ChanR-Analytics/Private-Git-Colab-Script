import os
import getpass

username = input("Please type in your username: ")
repository = input("Please type in the repository name you want to clone: ")
password = getpass.getpass("Please type in your password: ")

url = f"https://{username}:{password}@github.com/{username}/{repository}.git"

os.system(f"git clone {url}")
