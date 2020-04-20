import random


class WordGenerator:
    min_num_of_cards = 25
    static_word_bank = []
    dynamic_word_bank = []
    round_word_bank = []

    def __init__(self, static_word_bank_path, dynamic_word_bank):
        if static_word_bank_path is None and len(dynamic_word_bank) == 0:
            raise ValueError("Word Banks Are Empty")

        self.dynamic_word_bank = dynamic_word_bank
        self.static_word_bank = self.__read_static_word_bank__(static_word_bank_path)

        if len(self.static_word_bank) + len(self.dynamic_word_bank) < self.min_num_of_cards:
            raise ValueError("Word Banks Are to small! less than 25 words in both banks!")

    def __read_static_word_bank__(self, filepath):
        if filepath is None:
            return
        word_bank = []
        with open(filepath) as f:
            for line in f:
                word_bank.append(line.rstrip().split())
        return word_bank

    def get_cards(self):
        if len(self.dynamic_word_bank) == self.min_num_of_cards:
            return self.dynamic_word_bank
        if len(self.dynamic_word_bank) > self.min_num_of_cards:
            return random.sample(self.dynamic_word_bank, self.min_num_of_cards)
        else:
            num_of_static_cards_needed = self.min_num_of_cards - len(self.dynamic_word_bank)
            word_bank = self.dynamic_word_bank + random.sample(self.static_word_bank, num_of_static_cards_needed)
            return random.shuffle(word_bank)
