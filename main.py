y = 0
x = 1
board = [[0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]]
pieces = [[[1, 1], [1, 1]],
    [[0, 1], [1, 1]],
    [[1, 1], [0, 1]],
    [[0, 0], [1, 1]]]
rand = randint(0, 3)

def on_forever():
    global x, y, rand
    randp = pieces[rand]
    for i in range(len(randp)):
        for j in range(len(randp[i])):
            if(randp[i][j] == 1):
                led.plot(x + i, y + j)
    pause(1000)
    for i in range(len(randp)):
            for j in range(len(randp[i])):
                if(randp[i][j] == 1):
                    led.unplot(x + i, y + j)
    for j in range(2):
        if(randp[j][1] == 1 and (y + 1 == 4 or board[x + j][y + 2] == 1)):
            if(y <= 1): 
                gameover = True
            for i in range(len(randp)):
                for k in range(len(randp[i])):
                    if(randp[i][k] == 1):
                        board[x + i][y + k] = 1
                        led.plot(x + i, y + k)
            rand = randint(0, 3)
            y = -1
            x = 1

    y += 1
basic.forever(on_forever)