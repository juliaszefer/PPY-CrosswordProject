import re

import bcrypt

from Classes.Database import Database
from Classes.User import User


class LogIn:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    @staticmethod
    def login_logic(login, password):
        if Database.does_user_exists_by_login(login):
            _password = Database.get_user_password_by_login(login)
            password = bcrypt.hashpw(password.encode("utf-8"), _password[0:29].encode("utf-8")).decode("utf-8")

            if password == _password:
                user = Database.get_user(login)
                user = User(login, user[0], user[2], user[1], user[3])
                return user
            else:
                return "wrong password"
        else:
            return "wrong login"

    @staticmethod
    def register_logic(login, password):
        # password_salt = bcrypt.hashpw(password, bcrypt.gensalt())[0:29]
        if Database.does_user_exists_by_login(login):
            return "login already exists"
        password_pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
        if re.match(password_pattern, password) is None:
            return "wrong password"
        user = User(login, password)
        Database.insert_user(user)
        return user
