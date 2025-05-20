#setup x and y of piece start position, board is empty and represents microbit leds, pieces for each possible piece
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
#rand picks random piece out of 4 pieces, randp is the picked piece array
rand = randint(0, 3)
gameover = False
randp = pieces[rand]
#check if line cleared

def checkline():
    #checks every line to see if there is a line with a line clear
    for j in range(len(board[0])):
        for i in range(len(board)):
            #line is not fully filled
            if(board[i][j] == 0):
                break
            #line is fully filled
            else:
                if(i == 4 and board[i][j] == 1):
                    #this loop is to clear filled line
                    for k in range(5):
                        led.unplot(k, j)
                        board[k][j] = 0
                        #pause for effect
                        pause(200)
                    #this loop is to move lines above cleared line down 1, top line gets reset with 0
                    for l in range(5):
                        for m in range(j , 0 , -1):
                            if(m == 0):
                                board[l][m] = 0
                                led.unplot(l, m)
                            else:
                                board[l][m] = board[l][m - 1]
                                if(board[l][m] == 1):
                                    led.plot(l, m)
                                else:
                                    led.unplot(l, m)




def on_forever():
    global x, y, rand, gameover, randp
    #gameover code would clear screen then show sad face
    while gameover:
        basic.clear_screen()
        basic.show_icon(IconNames.SAD)
    #plot randp
    for i in range(len(randp)):
        for j in range(len(randp[i])):
            if(randp[i][j] == 1):
                led.plot(x + i, y + j)
    #pause to show piece
    pause(1000)
    #unplot randp
    for i in range(len(randp)):
            for j in range(len(randp[i])):
                if(randp[i][j] == 1):
                    led.unplot(x + i, y + j)
    #check if piece would collide with bottom or other board piece
    for j in range(len(randp)):
        for l in range(len(randp[j])):
            #if statement is true if there is collision
            if(randp[j][l] == 1 and (y + l == 4 or board[x + j][y + l + 1] == 1)):
                #gameover if new piece cannot fit
                if(y < 1):
                    gameover = True
                #change board to have piece on it also plots the piece on board
                for i in range(len(randp)):
                    for k in range(len(randp[i])):
                        if(randp[i][k] == 1):
                            board[x + i][y + k] = 1
                            led.plot(x + i, y + k)
                #set up new randp
                rand = randint(0, 3)
                y = -1
                x = 2
                randp = pieces[rand]
                #checks if line is clearable, too complex to put in so separated into new function, shouldve done this with more things
                checkline()
    #moves piece down one
    y += 1
basic.forever(on_forever)

#left right code
def on_button_pressed_a():
    global x, randp
    #move starts True
    move = True
    #if collision then don't move
    for i in range(len(randp)):
        for j in range(len(randp[i])):
            if(randp[i][j] == 1 and ( x + i == 0 or board[x + i - 1][y + j] == 1)):
                move = False
    #move if there is no collision
    if(move == True):
        #unplot
        for i in range(len(randp)):
                for j in range(len(randp[i])):
                    led.unplot(x + i, y + j)
        #move left
        x -= 1
        #plot
        for i in range(len(randp)):
            for j in range(len(randp[i])):
                if(randp[i][j] == 1):
                    led.plot(x + i, y + j)


input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global x, randp
    #move starts True
    move = True
    #if collision then don't move
    for i in range(len(randp)):
        for j in range(len(randp[i])):
            if(randp[i][j] == 1 and ( x + i == 4 or board[x + i + 1][y + j] == 1)):
                move = False
    if(move == True):
        #unplot
        for i in range(len(randp)):
                for j in range(len(randp[i])):
                    led.unplot(x + i, y + j)
        #move right
        x += 1
        #plot
        for i in range(len(randp)):
            for j in range(len(randp[i])):
                if(randp[i][j] == 1):
                    led.plot(x + i, y + j)
input.on_button_pressed(Button.B, on_button_pressed_b)

#rotate code
def on_button_pressed_ab():
    global randp,x ,y
    noblock = True
    #set temp to rotated randp
    temp = [[0,0],[0,0]]
    temp[0][0] = randp[1][0]
    temp[1][0] = randp[1][1]
    temp[1][1] = randp[0][1]
    temp[0][1] = randp[0][0]
    #check if temp would collide with existing board
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if(temp[i][j] == board[x + i][y + j] and temp[i][j] == 1):
                noblock = False
    #if there is no collision
    if(noblock):
        #unplot
        for i in range(len(randp)):
            for j in range(len(randp[i])):
                led.unplot(x + i, y + j)
        #set randp to rotated version
        randp = temp
        #plot
        for k in range(len(randp)):
            for l in range(len(randp[k])):
                if(randp[k][l] == 1):
                    led.plot(x + k, y + l)
input.on_button_pressed(Button.AB, on_button_pressed_ab)