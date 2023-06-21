import sqlite3

from Classes.Database import Database


class WordSet:
    def __init__(self, words, main_answer, theme, id_WordSet=-1, id_User=None):
        if id_WordSet == -1:
            self.id_WordSet = Database.get_max_idwordset() + 1
        else:
            self.id_WordSet = id_WordSet
        self.words = words
        self.main_answer = main_answer
        self.theme = theme
        self.id_User = id_User

    def get_wordSet_sql_data(self):
        data = (self.id_WordSet, self.main_answer, self.theme, self.id_User)
        return data

    def get_words_sql_data(self):
        data = []
        for word in self.words:
            data.append(word.get_sql_data())
        return data
