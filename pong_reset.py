import random

x = 0
pong_x = 0

y = 0
pong_y = 0

open("pong.csv", "w").write("pong_x,pong_y,bot_x,quality")

for i in range(3):
    x = random.randint(1,1000)
    y = random.randint(1, 100)

    pong_x = random.randint(1, 1000)
    pong_y = random.randint(1, 1000)

    open("pong.csv", "a").write("\n" + str(pong_x) + "," + str(pong_y) + "," + str(x) + "," + str(x-pong_y))