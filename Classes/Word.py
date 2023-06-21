import random

from Classes.Database import Database


class Word:
    def __init__(self, entry, clue, index, id_WordSet=-1, id_Word=-1):
        if id_Word == -1:
            self.id_Word = Database.get_max_idword() + 1
        else:
            self.id_Word = id_Word
        self.entry = entry.upper()
        self.shown_entry = list(self.__init_shown_entry())
        self.clue = clue
        self.key_index = index
        self.has_been_guessed_correctly = False
        if id_WordSet == -1:
            self.id_WordSet = Database.get_max_idwordset()+1
        else:
            self.id_WordSet = id_WordSet

    def get_shown_entry_string(self):
        return self.__list_to_string(self.shown_entry)

    def get_clue(self):
        return self.clue

    def get_points_for_word(self):
        return self.__get_n_of_not_shown_letters()

    def reveal_random_letter(self):
        not_shown_letters = self.__get_n_of_not_shown_letters()
        if not_shown_letters == 1:
            self.has_been_guessed_correctly = True
        if not_shown_letters <= 0:
            print("You cant show any more letters.")
            return False

        which_to_show = random.randrange(not_shown_letters)+1
        counter = 0
        for i in range(len(self.shown_entry)):
            if self.shown_entry[i] == "_":
                counter += 1
            if counter == which_to_show:
                self.shown_entry[i] = self.entry[i]
                break

        return True

    def __get_n_of_not_shown_letters(self):
        not_shown_letters = 0
        for i in range(len(self.shown_entry)):
            if self.shown_entry[i] == "_":
                not_shown_letters += 1
        return not_shown_letters

    def __init_shown_entry(self):
        shown_entry = ""
        for i in range(len(self.entry)):
            shown_entry += " _ "
        return shown_entry

    def __get_label(self):
        shown = self.__init_shown_entry()
        label_list = list(shown)
        return label_list

    def does_guess_match_entry(self, guess):
        if self.__list_to_string(self.entry) == guess.upper():
            self.reveal_whole_entry()
            self.has_been_guessed_correctly = True
            return self.__get_n_of_not_shown_letters()
        return 0

    def reveal_whole_entry(self):
        self.shown_entry = self.entry

    def get_sql_data(self):
        data = (self.id_Word, self.__list_to_string(self.entry), self.clue, self.key_index, self.id_WordSet)
        return data

    @staticmethod
    def __list_to_string(word_in_list):
        word = ""
        for letter in word_in_list:
            word += letter
        return word
