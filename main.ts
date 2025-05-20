// setup code
let y = 0
let x = 2
let board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
let pieces = [[[1, 1], [1, 1]], [[0, 1], [1, 1]], [[1, 1], [0, 1]], [[0, 0], [1, 1]]]
let rand = randint(0, 3)
let gameover = false
let randp = pieces[rand]
// check if line cleared
function checkline() {
    for (let j = 0; j < board[0].length; j++) {
        for (let i = 0; i < board.length; i++) {
            if (board[i][j] == 0) {
                break
            } else if (i == 4 && board[i][j] == 1) {
                for (let k = 0; k < 5; k++) {
                    led.unplot(k, j)
                    board[k][j] = 0
                    pause(200)
                }
                for (let l = 0; l < 5; l++) {
                    for (let m = j; m > 0; m += -1) {
                        if (m == 0) {
                            board[l][m] = 0
                            led.unplot(l, m)
                        } else {
                            board[l][m] = board[l][m - 1]
                            if (board[l][m] == 1) {
                                led.plot(l, m)
                            } else {
                                led.unplot(l, m)
                            }
                            
                        }
                        
                    }
                }
            }
            
        }
    }
}

basic.forever(function on_forever() {
    let i: number;
    let j: number;
    
    while (gameover) {
        basic.clearScreen()
        basic.showIcon(IconNames.Sad)
    }
    for (i = 0; i < randp.length; i++) {
        for (j = 0; j < randp[i].length; j++) {
            if (randp[i][j] == 1) {
                led.plot(x + i, y + j)
            }
            
        }
    }
    pause(1000)
    for (i = 0; i < randp.length; i++) {
        for (j = 0; j < randp[i].length; j++) {
            if (randp[i][j] == 1) {
                led.unplot(x + i, y + j)
            }
            
        }
    }
    for (j = 0; j < randp.length; j++) {
        for (let l = 0; l < randp[j].length; l++) {
            if (randp[j][l] == 1 && (y + l == 4 || board[x + j][y + l + 1] == 1)) {
                if (y < 1) {
                    gameover = true
                }
                
                for (i = 0; i < randp.length; i++) {
                    for (let k = 0; k < randp[i].length; k++) {
                        if (randp[i][k] == 1) {
                            board[x + i][y + k] = 1
                            led.plot(x + i, y + k)
                        }
                        
                    }
                }
                rand = randint(0, 3)
                y = -1
                x = 2
                randp = pieces[rand]
                checkline()
            }
            
        }
    }
    y += 1
})
// left right code
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    let i: number;
    let j: number;
    
    let move = true
    for (i = 0; i < randp.length; i++) {
        for (j = 0; j < randp[i].length; j++) {
            if (randp[i][j] == 1 && (x + i == 0 || board[x + i - 1][y + j] == 1)) {
                move = false
            }
            
        }
    }
    if (move == true) {
        for (i = 0; i < randp.length; i++) {
            for (j = 0; j < randp[i].length; j++) {
                led.unplot(x + i, y + j)
            }
        }
        x -= 1
        for (i = 0; i < randp.length; i++) {
            for (j = 0; j < randp[i].length; j++) {
                if (randp[i][j] == 1) {
                    led.plot(x + i, y + j)
                }
                
            }
        }
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    let i: number;
    let j: number;
    
    let move = true
    for (i = 0; i < randp.length; i++) {
        for (j = 0; j < randp[i].length; j++) {
            if (randp[i][j] == 1 && (x + i == 4 || board[x + i + 1][y + j] == 1)) {
                move = false
            }
            
        }
    }
    if (move == true) {
        for (i = 0; i < randp.length; i++) {
            for (j = 0; j < randp[i].length; j++) {
                led.unplot(x + i, y + j)
            }
        }
        x += 1
        for (i = 0; i < randp.length; i++) {
            for (j = 0; j < randp[i].length; j++) {
                if (randp[i][j] == 1) {
                    led.plot(x + i, y + j)
                }
                
            }
        }
    }
    
})
// rotate code
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    let i: number;
    let j: number;
    
    let noblock = true
    let temp = [[0, 0], [0, 0]]
    temp[0][0] = randp[1][0]
    temp[1][0] = randp[1][1]
    temp[1][1] = randp[0][1]
    temp[0][1] = randp[0][0]
    for (i = 0; i < temp.length; i++) {
        for (j = 0; j < temp[i].length; j++) {
            if (temp[i][j] == board[x + i][y + j] && temp[i][j] == 1) {
                noblock = false
            }
            
        }
    }
    if (noblock) {
        for (i = 0; i < randp.length; i++) {
            for (j = 0; j < randp[i].length; j++) {
                led.unplot(x + i, y + j)
            }
        }
        randp = temp
        for (let k = 0; k < randp.length; k++) {
            for (let l = 0; l < randp[k].length; l++) {
                if (randp[k][l] == 1) {
                    led.plot(x + k, y + l)
                }
                
            }
        }
    }
    
})
