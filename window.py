from tkinter import *
from tkinter import ttk
from snake import Snake
import random

def food():

    food_X = random.randint(0,49)
    food_Y = random.randint(0,49)

    food_X *= 10
    food_Y *= 10
    
    w.create_rectangle(food_X, food_Y,food_X+10,food_Y+10,fill="green",tags="food")

    cord = [food_X,food_Y]
    return cord

def move(direction,snake):
    
    global f 

    global left
    left = False

    global right
    right = False

    global up
    up = False

    global down
    down = False

    l,h = snake.Width+snake.Xstart,snake.Height+snake.Ystart

    if direction == 'left':
        snake.Xstart = snake.Xstart - 10
        l -= 10
        left = True
        window.after(100, move, direction, snake)
    elif direction == 'right':
        snake.Xstart = snake.Xstart + 10
        l += 10
        right = True
        window.after(100, move, direction, snake)  
    elif direction == 'up':
        snake.Ystart = snake.Ystart - 10
        h -= 10
        up = True
        window.after(100, move, direction, snake)
    else:
        snake.Ystart = snake.Ystart + 10
        h += 10
        down = True 
        window.after(100, move, direction, snake)
    
    
    w.delete("head")
    w.create_rectangle(snake.Xstart, snake.Ystart, l,h,fill=snake.Color, tags="head")


    if snake.Xstart == f[0] and snake.Ystart == f[1]:
        x_old = f[0]
        y_old = f[1]
        cord = [x_old, y_old]
        w.delete("food")
        print("Yummy!")
        f = food()
        body = snake.Body
        body.insert(0,cord)
        w.create_rectangle(cord[0], cord[1], cord[0] + 10, cord[1]+ 10,fill="white", tags=str(snake.Count))


window = Tk()
window.title("Snake game")
window.resizable(False, False)

w = Canvas (window, bg="black",height=500,width=500)
w.pack()
window.update()

snake = Snake(1)

l,h = snake.Width+snake.Xstart,snake.Height+snake.Ystart

w.create_rectangle(snake.Xstart, snake.Ystart, l,h,fill=snake.Color,tags="head")

f = food()

window.bind('<Left>', lambda event: move('left',snake))
window.bind('<Right>', lambda event: move('right',snake))
window.bind('<Up>', lambda event: move('up',snake))
window.bind('<Down>', lambda event: move('down',snake))


w.mainloop()

