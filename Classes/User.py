from Classes.Database import Database
import bcrypt


class User:
    def __init__(self, login, password, id_User=-1, points=0, id_Level=0):
        if id_User == -1:
            self.id_User = Database.get_max_iduser() + 1
        else:
            self.id_User = id_User
        self.userSettings = Database.get_usersettings(self.id_User)
        self.login = login
        self.password = bcrypt.hashpw(password.encode('utf-8'), b'$2b$12$CX01WWJ7/wm76.TyUIWU0.').decode('utf-8')
        self.points = points
        self.id_Level = id_Level

    def get_sql_data(self):
        data = (self.id_User, self.login, self.password, self.points, self.id_Level)
        return data

    def save_UserSettings(self):
        Database.update_usersettings(self.userSettings)

    def __str__(self):

        return f"login: {self.login}, pass: {self.password}, id: {self.id_User}, points: {self.points}"





