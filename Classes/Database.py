import sqlite3

from Classes.UserSettings import UserSettings


class Database:
    sql_directory = "Database_Sql_files/"
    database_file = "./Database/database"

    def __init__(self, version):
        self.__create_path = f"{Database.sql_directory}create_{version}.sql"
        self.__drop_path = f"{Database.sql_directory}drop_{version}.sql"

    def run_create(self):
        create_file = open(self.__create_path)

        con, cur = Database.get_connection_and_cursor()
        cur.executescript(create_file.read())

        Database.close_connection_and_cursor(con, cur)

    def run_drop(self):

        drop_file = open(self.__drop_path)
        con, cur = Database.get_connection_and_cursor()
        cur.executescript(drop_file.read())

        Database.close_connection_and_cursor(con, cur)

    @staticmethod
    def get_connection_and_cursor():
        con = sqlite3.connect(Database.database_file)
        cur = con.cursor()

        return con, cur

    @staticmethod
    def close_connection_and_cursor(con, cur):
        cur.close()
        con.close()

    @staticmethod
    def insert_WordSet(wordSet):
        con, cur = Database.get_connection_and_cursor()

        data = wordSet.get_wordSet_sql_data()
        try:
            cur.execute("INSERT INTO WordSet VALUES (?, ?, ?, ?)", data)
            con.commit()
        except sqlite3.IntegrityError:
            print("This WordSet already exists in the Database.")

        data = wordSet.get_words_sql_data()
        sql = f"INSERT INTO Word VALUES (?, ?, ?, ?, ?)"
        try:
            cur.executemany(sql, data)
            con.commit()
        except sqlite3.IntegrityError:
            print("This Word already exists in the Database.")

        Database.close_connection_and_cursor(con, cur)

    @staticmethod
    def get_max_idWordSet():
        con, cur = Database.get_connection_and_cursor()

        res = cur.execute("SELECT ifnull(max(id_WordSet), -1) from WordSet")
        id_wordSet = int(res.fetchone()[0])

        Database.close_connection_and_cursor(con, cur)
        return id_wordSet

    @staticmethod
    def get_max_idWord():
        con, cur = Database.get_connection_and_cursor()

        res = cur.execute("SELECT ifnull(max(id_Word), -1) from Word")
        id_word = int(res.fetchone()[0])

        Database.close_connection_and_cursor(con, cur)
        return id_word

    @staticmethod
    def insert_CompletedWordSets(id_User, id_WordSet):
        con, cur = Database.get_connection_and_cursor()

        data = (id_User, id_WordSet)
        try:
            cur.execute("INSERT INTO CompletedWordSets (id_User, id_WordSet) VALUES (?, ?)", data)
            con.commit()
        except sqlite3.IntegrityError:
            print("This CompletedWordSets already exists in the Database.")

        Database.close_connection_and_cursor(con, cur)

    @staticmethod
    def insert_User_Prize(id_User, id_Prize):
        con, cur = Database.get_connection_and_cursor()

        data = (id_User, id_Prize)
        try:
            cur.execute("INSERT INTO User_Prize (id_User, id_Prize) VALUES (?, ?)", data)
            con.commit()
        except sqlite3.IntegrityError:
            print("This User_Prize already exists in the Database.")

        Database.close_connection_and_cursor(con, cur)

    @staticmethod
    def insert_Scores(id_User, id_GameType, points, date):
        con, cur = Database.get_connection_and_cursor()

        res = cur.execute("SELECT ifnull(max(id_Scores), -1) from Scores")
        id_Scores = int(res.fetchone()[0]) + 1
        data = (id_Scores, id_User, id_GameType, points, date)
        cur.execute("INSERT INTO Scores VALUES (?, ?, ?, ?, ?)", data)
        con.commit()

        Database.close_connection_and_cursor(con, cur)

    @staticmethod
    def insert_User(user):
        con, cur = Database.get_connection_and_cursor()

        data = user.get_sql_data()
        try:
            cur.execute("INSERT INTO User VALUES (?, ?, ?, ?, ?)", data)
            con.commit()
        except sqlite3.IntegrityError:
            print("This User already exists in the Database.")

        Database.close_connection_and_cursor(con, cur)

    @staticmethod
    def get_max_idUser():
        con, cur = Database.get_connection_and_cursor()

        res = cur.execute("SELECT ifnull(max(id_User), -1) from User")
        id_User = int(res.fetchone()[0])

        Database.close_connection_and_cursor(con, cur)
        return id_User

    @staticmethod
    def insert_UserSettings(userSettings):
        con, cur = Database.get_connection_and_cursor()

        data = userSettings.get_sql_data()
        try:
            cur.execute("INSERT INTO UserSettings VALUES (?, ?, ?, ?)", data)
            con.commit()
        except sqlite3.IntegrityError:
            print("This UserSettings already exists in the Database.")

        Database.close_connection_and_cursor(con, cur)

    @staticmethod
    def get_UserSettings(id_User):
        con, cur = Database.get_connection_and_cursor()
        dataDict = {"id": id_User}

        res = cur.execute("SELECT id_Color_background, id_Color_outline, id_Color_font from UserSettings "
                          "WHERE id_User = :id", dataDict)

        data = res.fetchone()
        if data is None:
            print("No settings for this User in the Database, created a new set.")
            us = UserSettings(id_User)
        else:
            us = UserSettings(id_User, id_Color_bg=data[0], id_Color_outline=data[1], id_Color_font=data[2])

        Database.close_connection_and_cursor(con, cur)
        return us

    @staticmethod
    def update_UserSettings(userSettings):
        con, cur = Database.get_connection_and_cursor()

        data = userSettings.get_sql_data()
        dataDict = {
            "id": data[0],
            "bg": data[1],
            "ol": data[2],
            "fn": data[3]
        }

        cur.execute("UPDATE UserSettings "
                    "SET id_Color_background = :bg, id_Color_outline = :ol, id_Color_font = :fn "
                    "WHERE id_User = :id", dataDict)

        Database.close_connection_and_cursor(con, cur)




