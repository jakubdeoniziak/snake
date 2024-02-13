from tkinter import *
from tkinter import ttk
from snake import Snake
import random

def food():

    global cord

    food_X = random.randint(0,49)
    food_Y = random.randint(0,49)

    food_X *= 10
    food_Y *= 10
    
    w.create_rectangle(food_X, food_Y,food_X+10,food_Y+10,fill="green",tags="food")

    cord = [food_X,food_Y]

def move(snake):
    
    l = snake.Width+snake.Xstart
    h = snake.Height+snake.Ystart

    snake.Body[0] = [snake.Xstart, snake.Ystart,l,h]
    if direction == 'left':
        snake.Xstart = snake.Xstart - 10
        l -= 10
        snake.Body.insert(0,[snake.Xstart,snake.Ystart,l,h])
    elif direction == 'right':
        snake.Xstart = snake.Xstart + 10
        l += 10
        snake.Body.insert(0,[snake.Xstart,snake.Ystart,l,h])
    elif direction == 'up':
        snake.Ystart = snake.Ystart - 10
        h -= 10
        snake.Body.insert(0,[snake.Xstart,snake.Ystart,l,h])
    else:
        snake.Ystart = snake.Ystart + 10
        h += 10
        snake.Body.insert(0,[snake.Xstart,snake.Ystart,l,h])

    
    if snake.Xstart == cord[0] and snake.Ystart == cord[1]:
        w.delete("snake")
        for i in range(0,len(snake.Body)):
            w.create_rectangle(snake.Body[i][0], snake.Body[i][1], snake.Body[i][2],snake.Body[i][3],fill=snake.Color, tags="snake")
        #print(snake.Body)
    else:
        w.delete("snake")
        snake.Body.pop()
        for i in range(0,len(snake.Body)):
            w.create_rectangle(snake.Body[i][0], snake.Body[i][1], snake.Body[i][2],snake.Body[i][3],fill=snake.Color, tags="snake")

    if snake.Xstart == cord[0] and snake.Ystart == cord[1]: 
        w.delete("food")
        print("Yummy!")
        food()

    window.after(10, move, snake)

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
food()
move(snake)

l,h = snake.Width+snake.Xstart,snake.Height+snake.Ystart

w.create_rectangle(snake.Xstart, snake.Ystart, l,h,fill=snake.Color,tags="snake")

window.bind('<Left>', lambda event: change_move('left',snake))
window.bind('<Right>', lambda event: change_move('right',snake))
window.bind('<Up>', lambda event: change_move('up',snake))
window.bind('<Down>', lambda event: change_move('down',snake))

w.mainloop()
