#   a123_apple_1.py
import turtle
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)
wn.bgpic("background.gif")# Make the screen aware of the new file
apple = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()
def apple_down(active_apple):
  active_apple.penup()
  x_cord = active_apple.xcor()
  y_cord = active_apple.ycor()
  active_apple.goto(x_cord, y_cord - 160)



#-----function calls-----
draw_apple(apple)
apple_down(apple)
wn.mainloop()