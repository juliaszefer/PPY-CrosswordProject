class WordSet:
    def __init__(self, words, main_answer, theme):
        self.words = words
        self.main_answer = main_answer
        self.theme = theme

    def get_wordSet_sql_data(self, id_wordSet):
        data = (id_wordSet, self.main_answer, self.theme)
        return data

    def get_words_sql_data(self, id_word, id_wordSet):
        data = []
        for word in self.words:
            data.append(word.get_sql_data(id_word, id_wordSet))
            id_word += 1
        return data
