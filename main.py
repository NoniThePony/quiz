import pygame
from network import Network
import pickle
pygame.font.init()
import random



width = 900
height = 900
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Quiz")

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
p1Points = 0
p2Points = 0

#Button
class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 700
        self.height = 100

    # Button beschriften und ins Fenster Zeichnen
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render(self.text, 1, (0, 0, 0))
        win.blit(text, (self.x + round(self.width / 2) - round(text.get_width() / 2),
                        self.y + round(self.height / 2) - round(text.get_height() / 2)))

    # Ermöglicht den Button zu klicken
    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False

def redrawWindow(win, game, p, question, p1Points, p2Points):
    win.fill((128,128,128))

    if not(game.connected()):
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("Waiting for Player...", 1, (255,0,0), True)
        win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
    else:
        font = pygame.font.SysFont("comicsans", 10)
        text = font.render("Your Move", 1, (0, 255,255))
        win.blit(text, (105, 15))

    schrift =pygame.font.SysFont("comicsans", 30)
    text = schrift.render("Opponents", 1, (0, 255, 255))
    win.blit(text, (405, 15))

    questionT = font.render(question, 1, (0, 255, 255))
    win.blit(questionT, (20, 100))

    scorebord1 = font.render(str(p1Points), 1, (0, 255, 0))
    win.blit(scorebord1, (350, 50))

    scorebord2 = font.render(str(p2Points), 1, (0, 255, 0))
    win.blit(scorebord2, (450, 50))

    move1 = game.get_player_answer(0)
    move2 = game.get_player_answer(1)
    if game.bothWent():
        text1 = font.render(move1, 1, (0, 0, 0))
        text2 = font.render(move2, 1, (0, 0, 0))
    else:
        if game.p1Went and p == 0:
            text1 = font.render(move1, 1, (0, 0, 0))
        elif game.p1Went:
            text1 = font.render("Locked In", 1, (0, 0, 0))
        else:
            text1 = font.render("Waiting...", 1, (0, 0, 0))

        if game.p2Went and p == 1:
            text2 = font.render(move2, 1, (0, 0, 0))
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

questions = [["5x + 6 = 21", "Wx=1", "Wx=2", "Wx=4", "Rx=3"]]
questions.append(["Was ist die beste Programmiersprache?", "WJavascript", "WC", "Wphp", "RPython"])
questions.append(["In   Die Bieber bauen eine Burg", "erste person singular", "R", "-346°C", "-196°C"])



def neufrage(questions, randNum):
    Fragen = []
    for n in questions:
        Fragen.append(n)

    fragenText = Fragen[randNum][0]

    return fragenText

def neueAntworten(questions, randNum):
    Fragen = []
    for n in questions:
        Fragen.append(n)
    a1 = ""
    a2 = ""
    a3 = ""
    a4 = ""
    answers = []
    for i in range(1, 5):
        answers.append(questions[randNum][i])
    random.shuffle(answers)

    a1 = answers[0]
    a2 = answers[1]
    a3 = answers[2]
    a4 = answers[3]

    return [Button(a1, 25, 300, white), Button(a2, 25, 450, white), Button(a3, 25, 600, white), Button(a4, 25, 750, white)]

def returnrandNum():

    return random.randint(0, len(questions) - 1)

randNum = returnrandNum()
question = neufrage(questions, randNum)
btns = neueAntworten(questions, randNum)

def main():
    global p2Points, p1Points
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
            redrawWindow(win, game, player, question, p1Points, p2Points )
            pygame.time.delay(500)
            try:
                game = n.send("reset")
                returnrandNum()
                neufrage(questions, randNum)
                neueAntworten(questions, randNum)
            except:
                run = False
                print("Couldn't get game")
                break

            font = pygame.font.SysFont("comicsans", 90)
            if (game.winner() == 1 and player == 0) or (game.winner() == 2 and player == 1):
                text = font.render("Richtige Antwort !", 1, (255,0,0))
            elif game.winner() == 0:
                text = font.render("Falsche Antwort!", 1, (255,0,0))
            elif (game.winner() == 1 and player ==1) or (game.winner() == 2 and player == 0):
                text = font.render("Falsche Antwort!", 1, (255,0,0))
            elif (game.winner() == 3 ):
                text = font.render("Richtige Antwort !", 1, (255, 0, 0))

            else:
                text = font.render("Ich habe eine Möglichkeit vergessen", 1, (255, 0, 0))

            if (game.winner() == 1):
                p1Points = p1Points + 1
            elif (game.winner() == 2):
                p2Points = p2Points + 1
            elif (game.winner() == 3):
                p1Points = p1Points + 1
                p2Points = p2Points + 1

            else:
                p1Points = p1Points
                p2Points = p2Points

            win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(2000)

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
                                n.send(btn.text)

        redrawWindow(win, game, player, question, p1Points, p2Points)

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

