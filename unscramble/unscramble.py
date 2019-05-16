from itertools import permutations


class Unscramble:
    """To Do
    """

    def __init__(self, word):
        """To Do
        """
        self.word = word.lower()
        self.generate_words()

    def load_dictionary(self):
        """To Do
        """
        self.dictionary = ["hello", "world", "hell", "ehll", "ehl"]

    def get_word_lengths(self, upto):
        """ To Do
        """
        orig_word_len = len(self.word)
        word_lengths = list(reversed(range(orig_word_len + 1)))
        word_lengths = word_lengths[:-upto]
        return word_lengths

    def create_permutations(self, upto=3, exact_length=None):
        """To Do
        """
        self._all_permutations = []

        # Returns a list of int which specify word lengths
        self.word_lengths = self.get_word_lengths(upto)

        if exact_length is not None:
            self.word_lengths = [exact_length]

        for length in self.word_lengths:
            self.possible_words = permutations(self.word, length)
            self.possible_words = map(lambda x: "".join(x), list(self.possible_words))
            self.possible_words = list(self.possible_words)
            self._all_permutations.append(self.possible_words)

        self.possible_words = [
            word for word_list in self._all_permutations for word in word_list
        ]
        self.possible_words = list(set(self.possible_words))
        return self.possible_words

    def total_permutations(self):
        """To Do
        """
        return len(self.possible_words)

    def find_words(self):
        """To Do
        """
        self.actual_words = [
            word for word in self.possible_words if word in self.dictionary
        ]
        return self.actual_words

    def generate_words(self):
        """To Do
        """

        self.load_dictionary()
        self.create_permutations()
        #         self.dict_words = self.find_words()
        return self.find_words()
