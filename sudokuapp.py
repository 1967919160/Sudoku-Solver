from tkinter import *
import backtrack
import math

data = [[0,0,0,0,0,0,0,0,0], 
          [0,0,0,0,0,0,0,0,0], 
          [0,0,0,0,0,0,0,0,0], 
          [0,0,0,0,0,0,0,0,0], 
          [0,0,0,0,0,0,0,0,0], 
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0], 
          [0,0,0,0,0,0,0,0,0], 
          [0,0,0,0,0,0,0,0,0]]


def solveSudoku():
    global data
    if backtrack.solver(data) == False:
        return
    data = backtrack.solver(data)
    print(data)
    canvas.delete("numbers")
    fillNumbers(data)
    return 

def clearAll():
    global data
    for y in range(0, 9):
        for x in range(0, 9):
            data[y][x] = 0
    canvas.delete("numbers")
    fillNumbers(data)
    return 

window = Tk()
window.title("Sudoku Solver")
canvas = Canvas(width = 600, height = 600)
canvas.pack(fill=BOTH, side=TOP)

clearAll = Button(text = "Clear all.", command = clearAll)
clearAll.pack(fill=BOTH, side=BOTTOM)

solve = Button(text = "Solve", command = solveSudoku)
solve.pack(fill=BOTH, side=BOTTOM)


for i in range(10):
    color = "blue" if i % 3 == 0 else "gray"

    x0 = 50 + i * 55.5
    y0 = 50
    x1 = 50 + i * 55.5
    y1 = 600 - 50
    canvas.create_line(x0, y0, x1, y1, fill=color)

    x0 = 50
    y0 = 50 + i * 55.5
    x1 = 600 - 50
    y1 = 50 + i * 55.5
    canvas.create_line(x0, y0, x1, y1, fill=color)


numlst = []
def fillNumbers(data):
    global numlst
    numlst = []
    for row in range(9):
        for col in range(9):
            fill = data[row][col]
            x = 50 + col * 55.5 + 55.5 / 2
            y = 50 + row * 55.5 + 55.5 / 2
            numlst.append(canvas.create_text(x, y, text = fill, tags = "numbers"))
    return


row = -1
col = -1

def cellClicked(event):
    global row
    global col
    x, y = event.x, event.y
    if (50 < x < 600 - 50 and 50 < y < 600 - 50):
        canvas.focus_set() 
        row = math.floor((y - 50) / 55.5)
        col = math.floor((x - 50) / 55.5)
        drawCursor()

def drawCursor():
    global row
    global col
    canvas.delete("cursor")
    if row >= 0 and col >= 0:
        x0 = 50 + col * 55.5 
        y0 = 50 + row * 55.5 
        x1 = 50 + (col + 1) * 55.5 
        y1 = 50 + (row + 1) * 55.5 
        canvas.create_rectangle(x0, y0, x1, y1, outline="red", tags="cursor")


def keyPressed(event):
    global data
    global row
    global col
    global numlst
    if row >= 0 and col >= 0 and event.char in "1234567890":
        data[row][col] = int(event.char)
        x = 50 + col * 55.5 + 55.5 / 2
        y = 50 + row * 55.5 + 55.5 / 2
        canvas.delete(numlst[row * 9 + col])
        numlst[row * 9 + col] = canvas.create_text(x, y, text = int(event.char), tags = "numbers")




canvas.bind("<Button-1>", cellClicked)
canvas.bind("<Key>", keyPressed)



fillNumbers(data)
window.mainloop()