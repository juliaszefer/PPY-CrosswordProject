import sqlite3

from Classes.UserSettings import UserSettings


class Database:
    sql_directory = "../Database_Sql_files/"
    database_file = "../Database/database"

    def __init__(self, version):
        self.__create_path = f"{Database.sql_directory}create_{version}.sql"
        self.__drop_path = f"{Database.sql_directory}drop_{version}.sql"
        self.__seed_path = f"{Database.sql_directory}seed_{version}.sql"

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

    def run_seed(self):
        seed_file = open(self.__seed_path)
        con, cur = Database.get_connection_and_cursor()

        cur.executescript(seed_file.read())

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
    def get_level_by_id(id_level):
        con, cur = Database.get_connection_and_cursor()

        res = cur.execute(f"SELECT * FROM Level WHERE id_Level={id_level}")
        data = res.fetchone()

        return data

    @staticmethod
    def insert_wordset(wordSet):
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
    def get_max_idwordset():
        con, cur = Database.get_connection_and_cursor()

        res = cur.execute("SELECT ifnull(max(id_WordSet), -1) from WordSet")
        id_wordset = int(res.fetchone()[0])

        Database.close_connection_and_cursor(con, cur)
        return id_wordset

    @staticmethod
    def get_max_idword():
        con, cur = Database.get_connection_and_cursor()

        res = cur.execute("SELECT ifnull(max(id_Word), -1) from Word")
        id_word = int(res.fetchone()[0])

        Database.close_connection_and_cursor(con, cur)
        return id_word

    @staticmethod
    def insert_completedwordsets(id_User, id_WordSet):
        con, cur = Database.get_connection_and_cursor()

        data = (id_User, id_WordSet)
        try:
            cur.execute("INSERT INTO CompletedWordSets (id_User, id_WordSet) VALUES (?, ?)", data)
            con.commit()
        except sqlite3.IntegrityError:
            print("This CompletedWordSets already exists in the Database.")

        Database.close_connection_and_cursor(con, cur)

    @staticmethod
    def insert_user_prize(id_user, id_prize):
        con, cur = Database.get_connection_and_cursor()

        data = (id_user, id_prize)
        try:
            cur.execute("INSERT INTO User_Prize (id_User, id_Prize) VALUES (?, ?)", data)
            con.commit()
        except sqlite3.IntegrityError:
            print("This User_Prize already exists in the Database.")

        Database.close_connection_and_cursor(con, cur)

    @staticmethod
    def insert_scores(id_user, id_gametype, points, date):
        con, cur = Database.get_connection_and_cursor()

        res = cur.execute("SELECT ifnull(max(id_Scores), -1) from Scores")
        id_scores = int(res.fetchone()[0]) + 1
        data = (id_scores, id_user, id_gametype, points, date)
        cur.execute("INSERT INTO Scores VALUES (?, ?, ?, ?, ?)", data)
        con.commit()

        Database.close_connection_and_cursor(con, cur)

    @staticmethod
    def insert_user(user):
        con, cur = Database.get_connection_and_cursor()

        data = user.get_sql_data()
        try:
            cur.execute("INSERT INTO User VALUES (?, ?, ?, ?, ?)", data)
            con.commit()
        except sqlite3.IntegrityError:
            print("This User already exists in the Database.")

        Database.close_connection_and_cursor(con, cur)

    @staticmethod
    def get_user(login):
        con, cur = Database.get_connection_and_cursor()

        data_dict = {"login": login}
        res = cur.execute("SELECT password, points, id_User, id_Level FROM User WHERE login = :login", data_dict)
        data = res.fetchone()
        Database.close_connection_and_cursor(con, cur)

        return data

    @staticmethod
    def does_user_exists_by_login(login):
        con, cur = Database.get_connection_and_cursor()
        data_dict = {"login": login}

        res = cur.execute("SELECT * FROM User WHERE login = :login", data_dict)
        data = res.fetchone()
        Database.close_connection_and_cursor(con, cur)

        return not (data is None)

    @staticmethod
    def update_user_level(id_user):
        con, cur = Database.get_connection_and_cursor()
        data_dict = {"id_user": id_user}

        resp_points = cur.execute("SELECT points from User where id_User = :id_user", data_dict)
        data_points = resp_points.fetchone()[0]

        points_data_dict = {"data_points": data_points}

        res = cur.execute("SELECT MAX(id_Level) FROM Level "
                          "WHERE min_points <= :data_points "
                          "AND max_points > :data_points", points_data_dict)
        data_response = res.fetchone()[0]
        if data_response is None:
            resp_new_id = cur.execute("SELECT MAX(id_Level) FROM Level")
            data_new_id = resp_new_id.fetchone()[0]
            data_response = data_new_id

        up_data_dict = {"data_response": data_response, "id_user": id_user}
        cur.execute("UPDATE User SET id_Level = :data_response WHERE id_User = :id_user", up_data_dict)
        con.commit()

        Database.close_connection_and_cursor(con, cur)

    @staticmethod
    def get_user_password_by_login(login):
        con, cur = Database.get_connection_and_cursor()

        data_dict = {"login": login}
        res = cur.execute("SELECT password FROM User WHERE login = :login", data_dict)
        data = res.fetchone()[0]
        Database.close_connection_and_cursor(con, cur)

        return data

    @staticmethod
    def get_all_colors():
        con, cur = Database.get_connection_and_cursor()

        cur.execute("SELECT * FROM Color")
        rows = cur.fetchall()

        colors = [[row[0], row[1]] for row in rows]
        Database.close_connection_and_cursor(con, cur)

        return colors

    @staticmethod
    def get_color_by_id(id_color):
        con, cur = Database.get_connection_and_cursor()

        data_dict = {"id_color": id_color}
        res = cur.execute("SELECT name FROM Color WHERE id_Color = :id_color", data_dict)
        data = res.fetchone()[0]

        return data

    @staticmethod
    def get_all_wordsets(id_user):
        con, cur = Database.get_connection_and_cursor()

        data_dict = {"id_user": id_user}
        cur.execute("SELECT id_WordSet, theme FROM WordSet WHERE id_User IS NULL OR id_User = :id_user", data_dict)
        rows = cur.fetchall()

        wordsets = [[row[0], row[1]] for row in rows]
        Database.close_connection_and_cursor(con, cur)

        return wordsets

    @staticmethod
    def get_wordset_by_id(id_wordset):
        con, cur = Database.get_connection_and_cursor()

        data_dict = {"id_wordset": id_wordset}
        res = cur.execute("SELECT * FROM WordSet WHERE id_WordSet = :id_wordset", data_dict)
        data = res.fetchone()
        Database.close_connection_and_cursor(con, cur)

        return data

    @staticmethod
    def get_words_from_wordset_by_id(id_wordset):
        con, cur = Database.get_connection_and_cursor()

        data_dict = {"id_wordset": id_wordset}
        cur.execute("SELECT entry, clue, key_index FROM Word WHERE id_WordSet = :id_wordset", data_dict)
        rows = cur.fetchall()

        words = [[row[0], row[1], row[2]] for row in rows]
        Database.close_connection_and_cursor(con, cur)

        return words

    @staticmethod
    def get_all_users_points():
        con, cur = Database.get_connection_and_cursor()

        cur.execute("SELECT login, points FROM User")
        rows = cur.fetchall()

        user_points = [[row[0], row[1]] for row in rows]
        Database.close_connection_and_cursor(con, cur)

        return user_points

    @staticmethod
    def update_user_points_by_id(id_user, points):
        con, cur = Database.get_connection_and_cursor()

        data_dict = {"id_user": id_user, "points": points}
        cur.execute("UPDATE User SET points = points + :points WHERE id_User = :id_user", data_dict)
        con.commit()

        Database.close_connection_and_cursor(con, cur)

    @staticmethod
    def get_all_prizes_by_login(login):

        con, cur = Database.get_connection_and_cursor()

        data_dict = {"login": login}
        cur.execute("SELECT min_points, description FROM User U "
                    "JOIN User_Prize UP on U.id_User = UP.id_User "
                    "JOIN Prize P on UP.id_Prize = P.id_Prize WHERE U.login = :login", data_dict)
        rows = cur.fetchall()

        prizes = [[row[0], row[1]] for row in rows]
        Database.close_connection_and_cursor(con, cur)

        return prizes

    @staticmethod
    def get_all_prizes():
        con, cur = Database.get_connection_and_cursor()

        cur.execute("SELECT id_Prize, min_points FROM Prize")
        rows = cur.fetchall()

        prizes = [[row[0], row[1]] for row in rows]
        Database.close_connection_and_cursor(con, cur)

        return prizes

    @staticmethod
    def does_user_prize_exist(id_user, id_prize):
        con, cur = Database.get_connection_and_cursor()

        data_dict = {"id_user": id_user, "id_prize": id_prize}
        res = cur.execute("SELECT 1 FROM User_Prize WHERE id_User = :id_user and id_Prize = :id_prize", data_dict)
        data = res.fetchone()

        Database.close_connection_and_cursor(con, cur)
        return not (data is None)

    @staticmethod
    def get_max_iduser():
        con, cur = Database.get_connection_and_cursor()

        res = cur.execute("SELECT ifnull(max(id_User), -1) from User")
        id_user = int(res.fetchone()[0])

        Database.close_connection_and_cursor(con, cur)
        return id_user

    @staticmethod
    def insert_usersettings(userSettings):
        con, cur = Database.get_connection_and_cursor()

        data = userSettings.get_sql_data()
        try:
            cur.execute("INSERT INTO UserSettings VALUES (?, ?, ?, ?)", data)
            con.commit()
        except sqlite3.IntegrityError:
            print("This UserSettings already exists in the Database.")

        Database.close_connection_and_cursor(con, cur)

    @staticmethod
    def get_usersettings(id_User):
        con, cur = Database.get_connection_and_cursor()
        datadict = {"id": id_User}

        res = cur.execute("SELECT id_Color_background, id_Color_outline, id_Color_font from UserSettings "
                          "WHERE id_User = :id", datadict)

        data = res.fetchone()
        if data is None:
            print("No settings for this User in the Database, created a new set.")
            us = UserSettings(id_User)

            data_dict = {"id_user": us.id_User, "bg": us.id_Color_bg, "ol": us.id_Color_outline, "ft": us.id_Color_font}
            cur.execute("INSERT INTO UserSettings VALUES (:id_user, :bg, :ol, :ft)", data_dict)
            print("New userSettings set")
            con.commit()
        else:
            us = UserSettings(id_User, id_Color_bg=data[0], id_Color_outline=data[1], id_Color_font=data[2])

        Database.close_connection_and_cursor(con, cur)
        return us

    @staticmethod
    def update_usersettings(usersettings):
        con, cur = Database.get_connection_and_cursor()

        data = usersettings.get_sql_data()
        dataDict = {
            "id": data[0],
            "bg": data[1],
            "ol": data[2],
            "fn": data[3]
        }

        cur.execute("UPDATE UserSettings "
                    "SET id_Color_background = :bg, id_Color_outline = :ol, id_Color_font = :fn "
                    "WHERE id_User = :id", dataDict)
        con.commit()

        Database.close_connection_and_cursor(con, cur)
