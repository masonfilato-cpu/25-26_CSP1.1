# CODE TO ADD
#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
#Create SPYDER body
SPYDER = trtl.Turtle()
SPYDER.pensize(40)
SPYDER.circle(20)
#Configure SPYDER legs
num_legs = 8
LEG_LENGTH = 70
degree_of_legs_around = 360 / num_legs
leg = 0
print("z=",degree_of_legs_around)
print("z*n=", degree_of_legs_around*leg)
SPYDER.pensize(5)
#Draw legs
radius = 60
while leg < num_legs:
  SPYDER.goto(0, 20)
  if leg < 4:
    SPYDER.setheading(degree_of_legs_around * leg)
    SPYDER.pendown()
    SPYDER.circle(radius, 120)
    SPYDER.penup()
  else:
      SPYDER.setheading(radius*leg + 90)
      SPYDER.pendown()
      SPYDER.circle(radius, -120)
      SPYDER.penup()
leg = leg + 1
SPYDER.penup()
SPYDER.pencolor("white")
SPYDER.goto(-15,20)
SPYDER.pendown()
SPYDER.circle(3)
SPYDER.penup()
SPYDER.goto(15,20)
SPYDER.pendown()
SPYDER.circle(3)
SPYDER.hideturtle()
wn = trtl.Screen()
wn.mainloop()