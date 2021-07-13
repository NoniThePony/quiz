import random

class Game:
    def __init__(self, id):
        self.p1Went = False
        self.p2Went = False
        self.ready = False
        self.id = id
        self.answers = [None, None]
        self.wins = [0, 0]
        self.ties = 0
        self.pointsP1 = 0
        self.pointsP2 = 0
        self.questionnumber = random.randint(0, 2)

    def get_player_answer(self, p):  # p = 0 Spieler eins
        return self.answers[p]  # p = 1 Spieler zwei

    def play(self, player, answer):  # Checkt ob spieler geantwortet haben
        self.answers[player] = answer
        if player == 0:
            self.p1Went = True
        else:
            self.p2Went = True

    def pickquestion(self):
       return self.questionnumber


def connected(self):  # Checkt ob beide Spieler verbunden sind
    return self.ready


def bothWent(self):
    return self.p1Went and self.p2Went  # Sagt beide Spieler haben geantworted


def score(self):
    global p1, p2
    if p1 == 1:
        self.pointsP1 += 1
    elif p1 == 0:
        self.pointsP1 -= 1

    elif p2 == 1:
        self.pointsP2 += 1
    elif p2 == 0:
        self.pointsP2 -= 1


def resetanswerd(self):
    self.p1Went = False
    self.p2Went = False

