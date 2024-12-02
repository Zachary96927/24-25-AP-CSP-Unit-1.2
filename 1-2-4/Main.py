'''
import turtle as trtl

num_of_walls = 25

path width = 10

wall color = black

wall length = 10

loop num of wall times

     move wall length forward

     turn left

     add length of path to wall_length

     move wall ten forward

     pen up

     move wall ten forward

    pen down

   move wall forty forward

     turn left

   move to other side of the wall

  move back

   turn right



wn = turtl.screen()

wn.mainloop()
'''


import turtle as trtl
import random as rnd

#Initialize variables
wn = trtl.Screen()
maze_painter = trtl.Turtle()

num_of_walls = 25
path_width = 15
wall_color = "black"
wall_length = 15
maze_painter.pencolor(wall_color)
maze_painter.hideturtle()
maze_painter.speed(50)
def draw_barrier():
    maze_painter.right(90)
    maze_painter.forward(path_width)
    maze_painter.backward(path_width)
    maze_painter.left(90)
#repeat
for wall in range(num_of_walls):
    #Draw line
    maze_painter.forward(path_width)
    #turn left
    maze_painter.left(90)
    #increment
    wall_length += path_width
    #make door
    maze_painter.forward(wall_length/3)
    maze_painter.penup()
    maze_painter.forward(path_width)
    maze_painter.pendown()
    maze_painter.forward(wall_length-path_width-(wall_length/3))
    maze_painter.forward(wall_length)
    #draw barrier
    if (wall > 5):
        draw_barrier()




wn.listen()
wn.mainloop()