import random

x = 0
pong_x = 0

y = 0
pong_y = 0

open("pong.csv", "w").write("dir,pong_x,pong_y,bot_x,quality,win")

for i in range(3000):

    dir = random.randint(-1, 1)
    x = random.randint(1,1000) + 100 *dir
    y = random.randint(1, 100) + 100 *dir

    pong_x = random.randint(1, 1000)
    pong_y = random.randint(1, 1000)

    open("pong.csv", "a").write("\n" +str(dir)+","+ str(pong_x) + "," + str(pong_y) + "," + str(x) + "," + str(x-pong_y) + "," + str(abs(pong_x - y) > 500))
