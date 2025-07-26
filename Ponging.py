import pygame

import random

from sklearn import neighbors, metrics
from sklearn.model_selection import train_test_split
import pandas

knn = None

def setup_AI():

    global knn
    data = pandas.read_csv("pong.csv")
    print(data.columns)

    x = data[["pong_x", "pong_y" ,"bot_x"]].values
    y = data[["quality"]].values


    knn = neighbors.KNeighborsRegressor(n_neighbors=2, weights="uniform")
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2)

    knn.fit(x_train, y_train)
    #prediction = knn.predict(x_test)

    print("Test R^2 Score:", knn.score(x_test, y_test))

tick = 1

setup_AI()


def ai(x1,x2,x3):
    global tick
    if tick >= 60:
        tick = 1
        setup_AI()
        open("pong.csv", "a").write("\n" + str(pong.x) + "," + str(pong.y) + "," + str(bot.y) + "," + str(bot.y-pong.y))

    return knn.predict([[x1,x2,x3]])

pygame.init()

screen = pygame.display.set_mode((1000,1000))

player = pygame.rect.Rect(100,100,25,200)
bot = pygame.rect.Rect(900,100,25,200)
pong = pygame.rect.Rect(500,500,50,50)

x_dir = 1
y_dir = 0

while True:

    tick += 1
    pong.x += x_dir
    pong.y += y_dir


    if pong.colliderect(bot) or pong.colliderect(player):
        x_dir = -x_dir
        y_dir = random.randint(-1,1)

    if pong.y < 100 or pong.y > 900:
        y_dir = random.randint(-1,1)

    if pong.x < 0 or pong.x > 1000:
        pong.x = 500


    screen.fill("black")

    pygame.draw.rect(screen,(255,255,255),player)
    pygame.draw.rect(screen,(255,255,255),bot)
    pygame.draw.rect(screen,(255,255,255),pong)

    if ai(pong.x,pong.y,bot.y) > 0:
        bot.y -= 1

    if ai(pong.x, pong.y, bot.y) < 0:
        bot.y += 1

    if ai(pong.x,pong.y,player.y) > 0:
        bot.y -= 1

    if ai(pong.x, pong.y, player.y) < 0:
        bot.y += 1

    player.y = pong.y

    pygame.display.flip()

    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()