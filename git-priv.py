import os
import getpass

username = input("Please type in your username: ")
repository = input("Please type in the repository name you want to clone: ")
password = getpass.getpass("Please type in your password: ")
author_name = input("Please put in the repo's author username from whom you want to clone: ")
url1 = f"https://{username}:{password}@github.com/{author_name}/{repository}.git"
url2 = f"https://{username}:{password}@github.com/{username}/{repository}.git"
if username == author_name:
    os.system(f"git clone {url2}")
else:
    os.system(f"git clone {url1}") 
