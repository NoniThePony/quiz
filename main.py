import random
import pygame
from network import Network
import pickle
pygame.font.init()




width = 750
height = 900
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Quiz")

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

#Fragen
questions = [["5x + 6 = 21", "x=1", "x=2", "x=4", "x=3"]]
questions.append(["Was ist die beste Programmiersprache?", "Javascript", "C", "php", "Python"])
questions.append(["Bestimme die Personalform   Die Bieber bauen eine Burg", "erste person singular", "erste person plural", "drite person singular", "drite person plural"])

class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 600
        self.height = 100

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render(self.text, 1, (white))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False



class Quiz:
    def __init__(self, quest):

        self.Fragen = []
        for n in quest:
            self.Fragen.append(n)
        self.a1 = ""
        self.a2 = ""
        self.a3 = ""
        self.a4 = ""
        self.Ra = ""
        self.RaBtn = Button("", 50, 200, (white))
        self.antw1 = Button("", 50, 400, (white))
        self.antw2 = Button("", 50, 500, (white))
        self.antw3 = Button("", 50, 600, (white))
        self.antw4 = Button("", 50, 700, (white))

        self.lock = False
        self.right = 0

        self.nummer = 0
        self.Max = 3
        self.Frage()

    def Frage(self):
        questionnumber = game.pickquestion
        fragenText = self.Fragen[questionnumber][0]
        self.Ra = self.Fragen[questionnumber][-1]
        answers = []
        for i in range(1, 5):
            answers.append(self.Fragen[questionnumber][i])
        random.shuffle(answers)

        self.a1 = answers[0]
        self.a2 = answers[1]
        self.a3 = answers[2]
        self.a4 = answers[3]

        font = pygame.font.SysFont("comicsans", 80)
        text = font.render(fragenText, 1, (255, 255, 255))
        win.blit(text, (width / 2 - text.get_width() / 2, height / 6 - text.get_height() / 2))

        self.antw1 = Button(self.a1, 50, 400, (white))
        self.antw2 = Button(self.a2, 50, 500, (white))
        self.antw3 = Button(self.a3, 50, 600, (white))
        self.antw4 = Button(self.a4, 50, 700, (white))



        if self.a1 == self.Ra:
            self.RaBtn = self.antw1
        elif self.a2 == self.Ra:
            self.RaBtn = self.antw2
        elif self.a3 == self.Ra:
            self.RaBtn = self.antw3
        elif self.a4 == self.Ra:
            self.RaBtn = self.antw4
        self.Fragen.pop(questionnumber)

    def buttons(self):
        return [self.antw1, self.antw2, self.antw3 ,self.antw4]

    def control1(self):
        if self.lock == False:
            if self.Ra != self.a1:
                self.antw1 = Button(self.a1, 50, 400, (red))

            else:
                self.antw1 = Button(self.a1, 50, 400, (green))
                self.right += 1
            self.lock = True

    def control2(self):
        if self.lock == False:
            if self.Ra != self.a2:
                self.antw2 = Button(self.a2, 50, 400, (red))

            else:
                self.antw2 = Button(self.a2, 50, 400, (green))
                self.right += 1
            self.lock = True

    def control3(self):
        if self.lock == False:
            if self.Ra != self.a3:
                self.antw1 = Button(self.a3, 50, 400, (red))

            else:
                self.antw3 = Button(self.a3, 50, 400, (green))
                self.right += 1
            self.lock = True

    def control4(self):
        if self.lock == False:
            if self.Ra != self.a4:
                self.antw1 = Button(self.a4, 50, 400, (red))

            else:
                self.antw4 = Button(self.a4, 50, 400, (green))
                self.right += 1
            self.lock = True


    def getresult(self):
        return self.right
        self.right = 0




def quizCreator():
    q = Quiz(questions)
    btns = q.buttons


def redrawWindow(win, game, p):
    win.fill((128,128,128))

    if not(game.connected()):
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("Waiting for Player...", 1, (255,0,0), True)
        win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
    else:
        font = pygame.font.SysFont("comicsans", 10)
        text = font.render("Your Move", 1, (0, 255,255))
        win.blit(text, (80, 15))

        text = font.render("Opponents", 1, (0, 255, 255))
        win.blit(text, (380, 15))

        move1 = game.get_player_move(0)
        move2 = game.get_player_move(1)
        if game.bothWent():
            text1 = font.render(move1, 1, (0,0,0))
            text2 = font.render(move2, 1, (0, 0, 0))
        else:
            if game.p1Went and p == 0:
                text1 = font.render(move1, 1, (0,0,0))
            elif game.p1Went:
                text1 = font.render("Locked In", 1, (0, 0, 0))
            else:
                text1 = font.render("Waiting...", 1, (0, 0, 0))

            if game.p2Went and p == 1:
                text2 = font.render(move2, 1, (0,0,0))
            elif game.p2Went:
                text2 = font.render("Locked In", 1, (0, 0, 0))
            else:
                text2 = font.render("Waiting...", 1, (0, 0, 0))

        if p == 1:
            win.blit(text2, (100, 350))
            win.blit(text1, (400, 350))
        else:
            win.blit(text1, (100, 350))
            win.blit(text2, (400, 350))

        for btn in btns:
            btn.draw(win)

    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    player = int(n.getP())
    print("You are player", player)

    while run:
        clock.tick(60)
        try:
            game = n.send("get")
        except:
            run = False
            print("Couldn't get game")
            break

        if game.bothWent():
            redrawWindow(win, game, player)
            pygame.time.delay(500)
            try:
                game = n.send("reset")
            except:
                run = False
                print("Couldn't get game")
                break


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in btns:
                    if btn.click(pos) and game.connected():
                        if player == 0:
                            if not game.p1Went:
                                n.send(btn.text)
                        else:
                            if not game.p2Went:
                                n.send(q.getresult())

        redrawWindow(win, game, player)

def menu_screen():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        win.fill((128, 128, 128))
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Click to Play!", 1, (255,0,0))
        win.blit(text, (100,200))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    main()

while True:
    menu_screen()
