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
maze_painter.speed(10)
maze_painter.pensize(2)
def draw_barrier():
    maze_painter.right(90)
    maze_painter.forward(path_width*2)
    maze_painter.backward(path_width*2)
    maze_painter.left(90)

door = rnd.randint(path_width,(wall_length - path_width))
barrier = rnd.randint(path_width*2,(wall_length - path_width*2))

#repeat
for wall in range(num_of_walls):
    #Draw line
    maze_painter.forward(path_width)
    #make door
    maze_painter.penup()
    maze_painter.forward(path_width)
    maze_painter.pendown()
    draw_barrier()
    maze_painter.forward(wall_length-path_width-(wall_length/3))
    # turn left
    maze_painter.left(rnd.randint(90, 90))

    #increment
    wall_length += path_width
    #draw barrier





wn.listen()
wn.mainloop()