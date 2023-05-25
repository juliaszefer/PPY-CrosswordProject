import random


class Word:
    def __init__(self, entry, clue, index):
        self.__entry = list(entry.upper())
        self.__shown_entry = list(self.__init_shown_entry())
        self.__clue = clue
        self.key_index = index
        self.has_been_guessed_correctly = False
        self.key_index = index

    def get_shown_entry_string(self):
        return self.__list_to_string(self.__shown_entry)

    def get_clue(self):
        return self.__clue

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
        for i in range(len(self.__shown_entry)):
            if self.__shown_entry[i] == "_":
                counter += 1
            if counter == which_to_show:
                self.__shown_entry[i] = self.__entry[i]
                break

        return True

    def __get_n_of_not_shown_letters(self):
        not_shown_letters = 0
        for i in range(len(self.__shown_entry)):
            if self.__shown_entry[i] == "_":
                not_shown_letters += 1
        return not_shown_letters

    def __init_shown_entry(self):
        shown_entry = ""
        for i in range(len(self.__entry)):
            shown_entry += "_"
        return shown_entry

    def does_guess_match_entry(self, guess):
        if self.__list_to_string(self.__entry) == guess.upper():
            self.reveal_whole_entry()
            self.has_been_guessed_correctly = True
            return self.__get_n_of_not_shown_letters()
        return 0

    def reveal_whole_entry(self):
        self.__shown_entry = self.__entry

    def get_sql_data(self, id_word, id_wordSet):
        data = (id_word, self.__list_to_string(self.__entry), self.__clue, self.key_index, id_wordSet)
        return data

    @staticmethod
    def __list_to_string(word_in_list):
        word = ""
        for letter in word_in_list:
            word += letter
        return word

