import turtle as maze_painter

num_of_walls = 25
path_width = 10
wall_color = "black"
wall_length = 10
maze_painter.pencolor(wall_color)
maze_painter.hideturtle()
for num in range(num_of_walls):
    maze_painter.forward(wall_length)
    maze_painter.left(90)
    wall_length = wall_length + path_width
    maze_painter.forward(10)
    maze_painter.penup()
    maze_painter.forward(10)
    maze_painter.pendown()
    maze_painter.forward(40)
    maze_painter.left(90)
    maze_painter.forward(2*path_width)
    maze_painter.forward(2*-path_width)
    maze_painter.right(90)




wn = maze_painter.Screen()
wn.mainloop()