#setup code
y = 0
x = 2
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
gameover = False
randp = pieces[rand]
#check if line cleared

def checkline():
    for j in range(len(board[0])):
        for i in range(len(board)):
            if(board[i][j] == 0):
                break
            else: 
                if(i == 4 and board[i][j] == 1):
                    for k in range(5):
                        led.unplot(k, j)
                        board[k][j] == 0
                        pause(200)




def on_forever():
    global x, y, rand, gameover, randp
    while gameover:
        basic.clear_screen()
        basic.show_icon(IconNames.SAD)
    for i in range(len(randp)):
        for j in range(len(randp[i])):
            if(randp[i][j] == 1):
                led.plot(x + i, y + j)
    pause(1000)
    for i in range(len(randp)):
            for j in range(len(randp[i])):
                if(randp[i][j] == 1):
                    led.unplot(x + i, y + j)
    for j in range(len(randp)):
        for l in range(len(randp[j])):
            if(randp[j][l] == 1 and (y + l == 4 or board[x + j][y + l + 1] == 1)):
                if(y < 1): 
                    gameover = True
                for i in range(len(randp)):
                    for k in range(len(randp[i])):
                        if(randp[i][k] == 1):
                            board[x + i][y + k] = 1
                            led.plot(x + i, y + k)
                rand = randint(0, 3)
                y = -1
                x = 2
                randp = pieces[rand]
                checkline()
    y += 1
basic.forever(on_forever)

#left right code
def on_button_pressed_a():
    global x, randp
    move = True
    for i in range(len(randp)):
        for j in range(len(randp[i])):
            if(randp[i][j] == 1 and ( x + i == 0 or board[x + i - 1][y + j] == 1)):
                move = False
    if(move == True):
        for i in range(len(randp)):
                for j in range(len(randp[i])):
                    led.unplot(x + i, y + j)
        x -= 1
        for i in range(len(randp)):
            for j in range(len(randp[i])):
                if(randp[i][j] == 1):
                    led.plot(x + i, y + j)


input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global x, randp
    move = True
    for i in range(len(randp)):
        for j in range(len(randp[i])):
            if(randp[i][j] == 1 and ( x + i == 4 or board[x + i + 1][y + j] == 1)):
                move = False
    if(move == True):
        for i in range(len(randp)):
                for j in range(len(randp[i])):
                    led.unplot(x + i, y + j)
        x += 1
        for i in range(len(randp)):
            for j in range(len(randp[i])):
                if(randp[i][j] == 1):
                    led.plot(x + i, y + j)
input.on_button_pressed(Button.B, on_button_pressed_b)

#rotate code
def on_button_pressed_ab():
    global randp,x ,y
    noblock = True
    temp = [[0,0],[0,0]]
    temp[0][0] = randp[1][0]
    temp[1][0] = randp[1][1]
    temp[1][1] = randp[0][1]
    temp[0][1] = randp[0][0]
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if(temp[i][j] == board[x + i][y + j] and temp[i][j] == 1):
                noblock = False
    if(noblock):
        for i in range(len(randp)):
            for j in range(len(randp[i])):
                led.unplot(x + i, y + j)
        randp = temp
        for k in range(len(randp)):
            for l in range(len(randp[k])):
                if(randp[k][l] == 1):
                    led.plot(x + k, y + l)
input.on_button_pressed(Button.AB, on_button_pressed_ab)
