#   a123_apple_1.py
import turtle
import turtle as trtl
import random as rand
#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
wn = trtl.Screen()
ground_height = -160
apple_letter_x_offset = 15
apple_letter_y_offset = 30
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)
wn.bgpic("background.gif")# Make the screen aware of the new file
apple = trtl.Turtle()
letters = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()
  apple.penup()
  apple.color("blue")
  apple.write("A", font=("Arial", 30, "bold"))
  apple.goto(apple_letter_x_offset, apple_letter_y_offset)
def drop_down():
  apple.penup()
  apple.clear()
  apple.goto(apple.xcor(), ground_height)
  apple.hideturtle()
#   a123_apple_letters.py
#TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)
# a new location on the tree, only if the list of letters is not empty. Associate the
# turtle with a new letter selected at random from the list of letters
def tree(apple):
  if len(letters) > 0:
    newx = rand.randint(-200,200)
    newy = rand.randint(-10,30)
    new_letter = rand.choice(letters)


#TODO Create a function that takes a turtle (apple) and its corresponding letter from the letter
# list and draws that letter on that turtle (apple)
def letter_draw():
  apple.goto(newx , newy)
  apple.write(letters, font=("Arial", 30, "bold"))
#TODO Create a function that takes a turtle (apple) and its corresponding ltter from the letter
# list and set that turtle to be shaped by the image file, call the letter drawing function,
# and update the Screen

#TODO Iterate over the numbers from 0 to the number of apples, creating that many turtles
# calling your function that resets the apples by giving them a new random location
# add the new apples to a list of apples to be used in the rest of the program.
# The loop below executes the correct number of times by using the range() function
# to create a list of numbers to iterate over.
for i in range(0, number_of_apples):

#TODO Create a function that takes a letter as its parameter, uses that letter to retrieve the
# corresponding turtle (apple) and causes both to drop from the tree simultaneously. Once the
# apple and letter have dropped, call the apple reseting function.

#TODO define a function per letter that you will use in your program. Each function should check
# to see if the given letter is in the list of letters; if it is, it should drop the corresponding
# apple.

#TODO use the onkeypress method of wn to correlate the functions you defined above with each
# of the letters that the user might type.
# onkeypress requires that you name one function that must take
# no arguments to be called when the specified key is pressed.



#-----function calls-----

draw_apple(apple)
wn.onkeypress(drop_down, "a")
wn.listen()
wn.mainloop()