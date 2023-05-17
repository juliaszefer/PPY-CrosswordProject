import random


class Word:
    def __init__(self, entry, clue):
        self.__entry = list(entry.upper())
        self.__shown_entry = list(self.__init_shown_entry())
        self.__clue = clue
        self.has_been_guessed_correctly = False

    def get_shown_entry_string(self):
        return self.__list_to_string(self.__shown_entry)

    def get_clue(self):
        return self.__clue

    def get_points_for_word(self):
        return self.__get_n_of_not_shown_letters()

    def reveal_random_letter(self):
        not_shown_letters = self.__get_n_of_not_shown_letters()
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
        return self.__list_to_string(self.__entry) == guess.upper()

    def reveal_whole_entry(self):
        self.__shown_entry = self.__entry

    @staticmethod
    def __list_to_string(word_in_list):
        word = ""
        for letter in word_in_list:
            word += letter
        return word
