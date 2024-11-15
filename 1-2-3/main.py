#   a123_apple_1.py
import turtle
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
wn = trtl.Screen()
ground_height = -160
apple_letter_x_offset = 25
apple_letter_y_offset = 50
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)
wn.bgpic("background.gif")# Make the screen aware of the new file
apple = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()
  apple.penup()
  apple.color("blue")
  apple.write("A", font=("Arial", 31, "bold"))
  apple.goto(apple_letter_x_offset, apple_letter_y_offset)
def drop_down():
  apple.penup()

  apple.goto(apple.xcor(), ground_height)



#-----function calls-----

draw_apple(apple)
wn.onkeypress(drop_down, "a")
wn.listen()
wn.mainloop()