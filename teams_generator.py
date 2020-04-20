import random
import numpy as np


class Team:
    leader = None
    members = []

    def __init__(self, members):
        self.members = members


class TeamsGenerator:
    teams = {}

    def __init__(self, players):
        if len(players) < 4:
            raise ValueError("Not enough players! minimum players are 4")
        self.generate_teams(players)

    def generate_teams(self, players):
        self.teams["first"] = Team(random.sample(players, len(players)/2))
        self.teams["second"] = Team(players - self.first_team)

    def generate_team_leaders(self):
        self.__set_team_leader__("first")
        self.__set_team_leader__("second")

    def __set_team_leader__(self, team):
        self.teams[team].leader = random.choice(self.teams[team].members)






