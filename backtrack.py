sudoku = [[5,1,8,7,6,9,0,0,0], 
          [0,9,4,2,8,3,1,5,6], 
          [3,2,6,4,1,0,8,0,0], 
          [6,3,1,9,4,8,0,2,5], 
          [9,5,2,6,7,1,0,0,0], 
          [8,4,7,3,5,2,9,6,1],
          [4,7,9,0,3,6,5,0,2], 
          [2,6,5,0,9,7,0,0,0], 
          [1,8,3,5,2,4,6,0,0]]

sudoku2 = [[5,9,7,8,0,0,0,6,2], 
          [0,3,4,0,7,0,0,8,1], 
          [0,8,1,0,0,0,0,0,0], 
          [0,0,6,0,0,0,0,0,0], 
          [0,5,0,0,0,6,0,0,9], 
          [0,1,2,0,0,9,0,0,0], 
          [0,6,9,0,0,8,0,3,5], 
          [0,0,0,0,0,0,0,0,0], 
          [0,0,0,0,0,0,0,0,4]]

sudoku3 = [[0,0,0,0,0,0,0,0,0], 
          [0,0,0,0,0,0,0,0,0], 
          [0,0,0,0,0,0,0,0,0], 
          [0,0,0,0,0,0,0,0,0], 
          [0,0,0,0,0,0,0,0,0], 
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0], 
          [2,1,0,0,0,0,0,0,0], 
          [0,0,1,0,0,0,0,0,0]]


def checker(colNum, rowNum, n, data):
    for i in range(0,9):
        if data[rowNum][i] == n or data[i][colNum] == n:
            return False
    XinBox = (colNum // 3) * 3
    YinBox = (rowNum // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
          if data[YinBox + i][XinBox + j] == n:
            return False
    return True


def backtracking(data):
    for y in range(0,9):
        for x in range(0,9):
            if data[y][x] == 0:
                for i in range(1, 10):
                    if checker(x, y, i, data):
                        data[y][x] = i
                        if backtracking(data):
                            return True
                        data[y][x] = 0
                return False
    return True
            
def validSudoku(data):
    for y in range(0,9):
        for x in range(0,9):
            if data[y][x] != 0:
                for i in range(0,9):
                    if i != x:
                        if data[y][i] == data[y][x]:
                            return False
                    if i != y:
                        if data[i][x] == data[y][x]:
                            return False
                XinBox = (x // 3) * 3
                YinBox = (y // 3) * 3
                for i in range(0,3):
                    for j in range(0,3):
                        if YinBox + i != y and XinBox + j != x:
                            if data[YinBox + i][XinBox + j] == data[y][x]:
                                return False
    return True


def solver(data):
    retVal = data
    if validSudoku(data) == True:
        backtracking(data)
        return retVal
    else:
        print("Improper Sudoku")
        return False


