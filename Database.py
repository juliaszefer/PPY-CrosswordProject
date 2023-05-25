import sqlite3


class Database:
    def __init__(self, version):
        sql_directory = "Database_Sql_files/"
        self.__create_path = f"{sql_directory}create_{version}.sql"
        self.__drop_path = f"{sql_directory}drop_{version}.sql"

    def insert_WordSet(self, wordSet):
        con = sqlite3.connect("Database/database")
        cur = con.cursor()

        res = cur.execute("SELECT ifnull(max(id), -1) from WordSet")
        id_wordSet = int(res.fetchone()[0]) + 1
        data = wordSet.get_wordSet_sql_data(id_wordSet)
        cur.execute("INSERT INTO WordSet VALUES (?, ?, ?)", data)
        con.commit()

        res = cur.execute("SELECT ifnull(max(id), -1) from Word")
        id_word = int(res.fetchone()[0]) + 1
        data = wordSet.get_words_sql_data(id_word, id_wordSet)
        sql = f"INSERT INTO Word VALUES (?, ?, ?, ?, ?)"
        cur.executemany(sql, data)
        con.commit()

    def run_create(self):
        create_file = open(self.__create_path)
        con = sqlite3.connect("Database/database")
        cur = con.cursor()
        cur.executescript(create_file.read())

        cur.close()
        con.close()

    def run_drop(self):
        drop_file = open(self.__drop_path)
        con = sqlite3.connect("Database/database")
        cur = con.cursor()
        cur.executescript(drop_file.read())

        cur.close()
        con.close()




