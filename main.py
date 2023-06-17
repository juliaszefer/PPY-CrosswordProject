import os.path
import pathlib

from Classes.Database import Database
from Classes.User import User


def main():
    # database = Database("v04")

    user = User("login", "password", id_User=0)

    Database.insert_User(user)
    Database.insert_UserSettings(user.userSettings)
    print(user)


if __name__ == '__main__':
    main()
