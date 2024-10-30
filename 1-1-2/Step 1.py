# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = "pink"
spot_size = 2
spot_shape = "circle"
score = 0
#-----initialize turtle-----
spot = trtl.Turtle()
spot.color(spot_color)
spot.shapesize(spot_size)
spot.shape(spot_shape)
spot.penup()
score_writer = trtl.Turtle()
score_writer.penup()
score_writer.goto(420,370)
#-----game functions--------
def spot_clicked(x,y):
    print("Hello")
def change_position(x,y):
    new_xpos = rand.randint(-400,400)
    new_ypos = rand.randint(-300,300)
    spot.goto(new_xpos, new_ypos)
def update_score(x,y):
    global score
    score += 1
    print(score)
def font_setup("Arial", 20, "normal"):


#-----events----------------
spot.onclick(change_position)
spot.onclick(update_score)
wn = trtl.Screen()
wn.mainloop()