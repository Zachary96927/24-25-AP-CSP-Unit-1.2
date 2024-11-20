#   a123_apple_1.py
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
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "W", "X", "Y", "Z"]
apple_letters = ["A"]

number_of_apples = len(letters)
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(apple):
  apple.shape(apple_image)
  wn.update()
  apple.showturtle()
  apple.penup()
  apple.color("blue")
  apple.write("A", font=("Arial", 30, "bold"))
  apple.goto(apple_letter_x_offset, apple_letter_y_offset)
def drop_apple():
  apple.penup()
  apple.clear()
  apple.goto(apple.xcor(), ground_height)
  apple.hideturtle()
  apple_letters.pop()
  reset_apple(apple)
#   a123_apple_letters.py
#TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)
# a new location on the tree, only if the list of letters is not empty. Associate the
# turtle with a new letter selected at random from the list of letters
def reset_apple(apple):
  if len(letters) > 0:
    newx = rand.randint(-200,200)
    newy = rand.randint(-10,30)
    new_letter = rand.randint(0,len(letters))
    apple.goto(newx, newy)
    apple.letters.append(str(new_letter))
    draw_apple(apple, letters.pop(new_letter))



#TODO Create a function that takes a turtle (apple) and its corresponding letter from the letter
# list and draws that letter on that turtle (apple)
def letter_draw(apple, letter):
  apple.write(rand.choice(letters), font=("Arial", 30, "bold"))
#TODO Create a function that takes a turtle (apple) and its corresponding ltter from the letter
# list and set that turtle to be shaped by the image file, call the letter drawing function,
# and update the Screen
def new_apple():
  apple.shape(apple_image)
  apple.showturtle()
  wn.update()

#TODO Iterate over the numbers from 0 to the number of apples, creating that many turtles
# calling your function that resets the apples by giving them a new random location
# add the new apples to a list of apples to be used in the rest of the program.
# The loop below executes the correct number of times by using the range() function
# to create a list of numbers to iterate over.
'''
for i in range(0, number_of_apples):
  reset_apple(apple)
'''


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

def check_apple_a():
  if("A" in apple_letters):
    drop_apple()
def check_apple_b():
  if("B" in apple_letters):
    drop_apple()
def check_apple_c():
  if("C" in apple_letters):
    drop_apple()
def check_apple_d():
  if("D" in apple_letters):
    drop_apple()
def check_apple_e():
  if("E" in apple_letters):
    drop_apple()
def check_apple_f():
  if("F" in apple_letters):
    drop_apple()
def check_apple_g():
  if("G" in apple_letters):
    drop_apple()
def check_apple_h():
  if("H" in apple_letters):
    drop_apple()
def check_apple_i():
  if("I" in apple_letters):
    drop_apple()
def check_apple_j():
  if("J" in apple_letters):
    drop_apple()
def check_apple_k():
  if("K" in apple_letters):
    drop_apple()
def check_apple_l():
  if("L" in apple_letters):
    drop_apple()
def check_apple_m():
  if("M" in apple_letters):
    drop_apple()
def check_apple_n():
  if("N" in apple_letters):
    drop_apple()
def check_apple_o():
  if("O" in apple_letters):
    drop_apple()
def check_apple_p():
  if("P" in apple_letters):
    drop_apple()
def check_apple_q():
  if("Q" in apple_letters):
    drop_apple()
def check_apple_r():
  if("R" in apple_letters):
    drop_apple()
def check_apple_s():
  if("S" in apple_letters):
    drop_apple()
def check_apple_t():
  if("T" in apple_letters):
    drop_apple()
def check_apple_u():
  if("U" in apple_letters):
    drop_apple()
def check_apple_v():
  if("V" in apple_letters):
    drop_apple()
def check_apple_w():
  if("W" in apple_letters):
    drop_apple()
def check_apple_x():
  if("X" in apple_letters):
    drop_apple()
def check_apple_y():
  if("Y" in apple_letters):
    drop_apple()
def check_apple_z():
  if"Z" in apple_letters:
    drop_apple()

#-----function calls-----

draw_apple(apple)
wn.onkeypress(check_apple_a, "a")
wn.onkeypress(check_apple_b, "b")
wn.onkeypress(check_apple_c, "c")
wn.onkeypress(check_apple_d, "d")
wn.onkeypress(check_apple_e, "e")
wn.onkeypress(check_apple_f, "f")
wn.onkeypress(check_apple_g, "g")
wn.onkeypress(check_apple_h, "h")
wn.onkeypress(check_apple_i, "i")
wn.onkeypress(check_apple_j, "j")
wn.onkeypress(check_apple_k, "k")
wn.onkeypress(check_apple_l, "l")
wn.onkeypress(check_apple_m, "m")
wn.onkeypress(check_apple_n, "n")
wn.onkeypress(check_apple_o, "o")
wn.onkeypress(check_apple_p, "p")
wn.onkeypress(check_apple_q, "q")
wn.onkeypress(check_apple_r, "r")
wn.onkeypress(check_apple_s, "s")
wn.onkeypress(check_apple_t, "t")
wn.onkeypress(check_apple_u, "u")
wn.onkeypress(check_apple_v, "v")
wn.onkeypress(check_apple_w, "w")
wn.onkeypress(check_apple_x, "x")
wn.onkeypress(check_apple_y, "y")
wn.onkeypress(check_apple_z, "z")




wn.listen()
wn.mainloop()