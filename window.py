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
    
    snake.Body[0] = [snake.Xstart, snake.Ystart]

    w.delete("head")
    w.create_rectangle(snake.Xstart, snake.Ystart, l,h,fill=snake.Color, tags="head")

    if snake.Xstart == f[0] and snake.Ystart == f[1]:
        cords = [snake.Xstart, snake.Ystart]
        w.delete("food")
        print("Yummy!")

        
        for i in range(2,len(snake.Body)):
            snake.Body[i] = snake.Body[i-1]

        if direction == 'down':
            w.create_rectangle(cords[0], cords[1] - 10, cords[0] + 10, cords[1],fill=snake.Color, tags="snake")
            snake.Body.append([cords[0],cords[1] - 10])
        elif direction == 'up':
            w.create_rectangle(cords[0], cords[1] + 10, cords[0] + 10, cords[1] + 20,fill=snake.Color, tags="snake")
            snake.Body.append([cords[0],cords[1] + 10])
        elif direction == 'right':
            snake.Body.append([cords[0] - 10,cords[1]])
            w.create_rectangle(cords[0] - 10, cords[1], cords[0], cords[1] + 10,fill=snake.Color, tags="snake")
        elif direction == 'left':
            w.create_rectangle(cords[0] + 10, cords[1], cords[0] + 20, cords[1] + 10,fill=snake.Color, tags="snake")
            snake.Body.append([cords[0] + 10,cords[1]])
        
        f = food()
        print(snake.Body)
    
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

l,h = snake.Width+snake.Xstart,snake.Height+snake.Ystart

w.create_rectangle(snake.Xstart, snake.Ystart, l,h,fill=snake.Color,tags="head")


window.bind('<Left>', lambda event: change_move('left',snake))
window.bind('<Right>', lambda event: change_move('right',snake))
window.bind('<Up>', lambda event: change_move('up',snake))
window.bind('<Down>', lambda event: change_move('down',snake))

w.mainloop()

