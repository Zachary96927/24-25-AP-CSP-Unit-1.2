import turtle as trtl



x = 10

for num in range(20):
    trtl.forward(x)
    trtl.left(90)
    x = x + 10

wn = trtl.Screen()
wn.mainloop()