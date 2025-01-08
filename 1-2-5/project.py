

# Import Statements
import turtle as trtl
import random as rand

# Variables
lock = True
player_id = [1,2]
timer = rand.randint(5,10)
wn=trtl.Screen()
wn.setup(width=558, height=345)
counter_display = trtl.Turtle()
counter_display.color("black")
counter_interval = 1000
font_setup=("Arial", 20, "normal")

timer_up = False
player1=trtl.Turtle()
player2=trtl.Turtle()
lazer1 = trtl.Turtle()
lazer2 = trtl.Turtle()
hour_list = ['1:','2:','3:','4:','5:','6:','7:','8:','9:','10:','11:','12:']
minute_list = ["01","02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58" "59", "60"]
day_list = ["AM", "PM"]
hour = rand.choice(hour_list)
minute = rand.choice(minute_list)
day = rand.choice(day_list)
wn.setup(558,345)
# Turtle Setup
counter_display.speed(100)
counter_display.penup()
counter_display.goto(100,100)
counter_display.write("It's "+ hour + minute + " " + day, font = font_setup)
counter_display.goto(-100, -100)

wn.mainloop()