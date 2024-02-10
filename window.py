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

def move(snake):
    
    global f 

    l = snake.Width+snake.Xstart
    h = snake.Height+snake.Ystart

    

    if direction == 'left':
        snake.Xstart = snake.Xstart - 10
        l -= 10
    elif direction == 'right':
        snake.Xstart = snake.Xstart + 10
        l += 10 
    elif direction == 'up':
        snake.Ystart = snake.Ystart - 10
        h -= 10
    else:
        snake.Ystart = snake.Ystart + 10
        h += 10
    
    w.delete("head")
    w.create_rectangle(snake.Xstart, snake.Ystart, l,h,fill=snake.Color, tags="head")

    if snake.Xstart == f[0] and snake.Ystart == f[1]:
        w.delete("food")
        print("Yummy!")
        f = food()
        snake.Body.append(cords)
        #print(snake.Body)
        
    # for food_X, food_Y in body:
    #     w.create_rectangle(f[0], f[1], f[0] + 10, f[1] + 10,fill=snake.Color, tags="snake")
    #     body.append[w]

    
    window.after(100, move, snake)

def change_move(new_direction,snake):

    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction


def cord(snake):
    
    global cords

    cords = [snake.Xstart, snake.Ystart]


    if cords[0] == f[0] and cords[1] == f[1]:
        #w.create_rectangle(f[0] + 10, f[1], f[0] + 10, f[1],fill=snake.Color, tags="snake")
        snake.Body.append(cords)
        

    # snake.Body[0] = cord
    print(cords)
    
    window.after(100, cord, snake)
    
window = Tk()
window.title("Snake game")
window.resizable(False, False)

w = Canvas (window, bg="black",height=500,width=500)
w.pack()
window.update()

direction = "down"

snake = Snake(1)
f = food()
move(snake)

cord(snake)

l,h = snake.Width+snake.Xstart,snake.Height+snake.Ystart

w.create_rectangle(snake.Xstart, snake.Ystart, l,h,fill=snake.Color,tags="head")


window.bind('<Left>', lambda event: change_move('left',snake))
window.bind('<Right>', lambda event: change_move('right',snake))
window.bind('<Up>', lambda event: change_move('up',snake))
window.bind('<Down>', lambda event: change_move('down',snake))

w.mainloop()

