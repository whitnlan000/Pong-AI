import pygame

import random
import winsound

from sklearn import neighbors, metrics
from sklearn.model_selection import train_test_split
import pandas

knn = None

def setup_AI():

    global knn
    data = pandas.read_csv("pong.csv")

    x = data[["dir","pong_x", "pong_y" ,"bot_x" , "win"]].values
    y = data[["quality"]].values


    knn = neighbors.KNeighborsRegressor(n_neighbors=2, weights="uniform")
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2)

    knn.fit(x_train, y_train)


tick = 1



player_score = 0
bot_score = 0

setup_AI()

y_dir = 0
pygame.font.init()

score = pygame.font.SysFont("Arial",36)

def ai(x1,x2,x3,win):
    global tick
    global y_dir
    if tick >= 10:
        tick = 1
        setup_AI()
        open("pong.csv", "a").write("\n" + str(y_dir)+"," + str(pong.x) + "," + str(pong.y) + "," + str(bot.y) + "," + str(bot.y-pong.y) + "," + str(abs(pong.x - player.y) > 500))

    return knn.predict([[y_dir,x1,x2,x3,win]])

pygame.init()

screen = pygame.display.set_mode((1000,1000))

player = pygame.rect.Rect(100,100,5,200)
bot = pygame.rect.Rect(900,100,5,200)
pong = pygame.rect.Rect(500,500,25,25)

x_dir = 1.5
y_dir = 0
scoredisp = "0-0"

while True:
    print(x_dir)
    tick += 1
    pong.x += x_dir
    pong.y += y_dir

    if x_dir > 23:
        x_dir = 23

    if pong.colliderect(player):
        winsound.PlaySound("1.mp3.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

        x_dir = abs(x_dir*1.02)
        y_dir = random.randint(-2,2)

    if pong.colliderect(bot):
        winsound.PlaySound("3.mp3.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

        x_dir = -abs(x_dir*1.02)
        y_dir = random.randint(-2,2)

    if pong.y < 100:
        y_dir = 1
    if pong.y > 900:
        y_dir = -1

    if pong.x < 0:
        pong.x = 500
        pong.y = player.y
        player_score += 1
        print(str(player_score) + "-" + str(bot_score))
    if pong.x > 1000:
        pong.x = 500
        pong.y = bot.y
        bot_score += 1
        print(str(player_score) + "-" + str(bot_score))

    scoredisp = str(player_score) + "-" + str(bot_score)

    screen.fill("black")
    screen.blit(score.render(scoredisp,False,"white"),(500,500))


    pygame.draw.rect(screen,(255,255,255),player)
    pygame.draw.rect(screen,(255,255,255),bot)
    pygame.draw.rect(screen,(255,255,255),pong)

    speedz = (abs(pong.x - player.y) > 500) + 2
    #print(speedz)
    if speedz == 0:
        print("FREEZE!")
    #print(abs(pong.x - player.y))
    #print(speedz)

    prediction = ai(pong.x, pong.y, bot.y, pong.x > 900)

    if prediction > 0:
        bot.y -= speedz
    elif prediction < 0:
        bot.y += speedz

    #if pong.y >= player.y:
    #    player.y += 2
    #else:
    #    player.y -= 2
    if pygame.key.get_pressed()[pygame.K_UP]:
        player.y -= 2
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        player.y += 2

    pygame.display.flip()

    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
        if event == pygame.K_UP:
            player.y += 2

        if event == pygame.K_DOWN:
            player.y -= 2
