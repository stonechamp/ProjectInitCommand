import sys
import os
from github import Github

path = "/Users/kalle/Documents/Projects/MyProjects/"

username = ""
password = ""


def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + str(sys.argv[1]))
    user = Github(username, password).get_user()
    repo = user.create_repo(sys.argv[1])
    print("Succesfully created repository {}".format(sys.argv[1]))


if __name__ == "__main--":
    create()
