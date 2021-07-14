import random

class Game:
    def __init__(self, id):
        self.p1Went = False
        self.p2Went = False
        self.ready = False
        self.id = id
        self.answers = [None, None]
        self.wins = [0,0]
        self.ties = 0
        self.questionnumber = random.randint(0, 2)

    # p = 0 Spieler eins   p = 1 Spieler zwei parameter p [0, 1]
    #richtig oder Falsche Antwort return = R oder W
    def get_player_answer(self, p):
        return self.answers[p]

    # Checkt ob spieler geantwortet haben
    # Setzt p1Went oder p2Went auf True wen der entsprechende Spieler geantworted hat.
    def play(self, player, move):
        self.answers[player] = move
        if player == 0:
            self.p1Went = True
        else:
            self.p2Went = True

    def pickquestion(self):
       return self.questionnumber

    # Checkt ob beide Spieler verbunden sind
    def connected(self):
        return self.ready

    # Sagt beide Spieler haben geantworted
    def bothWent(self):
        return self.p1Went and self.p2Went


    #Überprüft ob die speiler Richtig oder Falsch geantworted haben und dated den score up.
    # R ist Richtig W ist Falsch
    # 0 =  beide Flasch
    # 1 = p1 score + 1
    # 2 = p2 score + 1
    # 3 = p1 score + 1 und 2 score + 1
    def winner(self):

        p1 = self.answers[0].upper()[0]
        p2 = self.answers[1].upper()[0]

        winner = 0

        if p1 == "W" and p2 == "W":
            winner = 0
        elif p1 == "R" and p2 == "W":
            winner = 1
        elif p1 == "W" and p2 == "R":
            winner = 2
        elif p1 == "R" and p2 == "R":
            winner = 3

        return winner




    def resetanswerd(self):
        self.p1Went = False
        self.p2Went = False
        self.questionnumber = random.randint(0, 2)



