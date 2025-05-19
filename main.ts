let y = 0
let x = 1
let board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
let pieces = [[[1, 1], [1, 1]], [[0, 1], [1, 1]], [[1, 1], [0, 1]], [[0, 0], [1, 1]]]
let rand = randint(0, 3)
basic.forever(function on_forever() {
    let i: number;
    let j: number;
    let gameover: boolean;
    
    let randp = pieces[rand]
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
    for (j = 0; j < 2; j++) {
        if (randp[j][1] == 1 && (y + 1 == 4 || board[x + j][y + 2] == 1)) {
            if (y <= 1) {
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
            x = 1
        }
        
    }
    y += 1
})
