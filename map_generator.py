import random
import numpy as np


class MapGenerator:
    cards_map = []
    min_num_of_cards = 25
    map_colors = {
        "first_team": "Red",
        "second_team": "Blue",
        "black_spy": "Black",
        "bystanders": "Brown"
    }
    num_of_cards = {
        "first_team": 9,
        "second_team": 8,
        "black_spy": 1,
        "bystanders": 7
    }

    def __init__(self, starting_team):
        self.map_colors["first_team"] = starting_team
        self.map_colors["second_team"] = "Blue" if starting_team == "Red" else "Red"

    def generate_map(self):
        cards_map = [None] * self.min_num_of_cards
        map_indexs = list(range(self.min_num_of_cards))
        first_team_cards = random.sample(map_indexs, self.num_of_cards["first_team"])
        map_indexs -= first_team_cards
        second_team_cards = random.sample(map_indexs, self.num_of_cards["second_team"])
        map_indexs -= second_team_cards
        black_card = random.choice(map_indexs)
        map_indexs -= black_card
        bystander_cards = map_indexs

        cards_map[first_team_cards] = self.map_colors["first_team"]
        cards_map[second_team_cards] = self.map_colors["second_team"]
        cards_map[black_card] = self.map_colors["black_spy"]
        cards_map[bystander_cards] = self.map_colors["bystanders"]

        return np.reshape(cards_map, (5, 5))





