import turtle
import random
import field


def kick():
    ball.setheading(180)
    angle = random.randint(0, 27)  # select a random angle for the ball to be kicked.
    direction = random.randint(0, 1)  # select if the ball should go left or right

    if direction == 0:  # if the direction is 0 kick the ball left by the random angle
        ball.left(angle)
    else:
        ball.right(angle)  # if the direction is 1 kick the ball right by the random angle
    ball.forward(320)  # move the ball forward towards the goals

    if goalie.distance(ball) < 35:  # if the goalie is within 35 pixels of the ball it is a save.
        ball.write("SAVE")  # write "save" where the ball was saved
        ball.setheading(180)
        ball.backward(250)
    else:  # else if the goalie is further than 35 pixels away from the ball it is a goal.
        ball.write("GOAL")  # write "goal" where the goal was saved

    ball.hideturtle()  # hide the ball while it goes back to the centre of the field.
    ball.speed(0)
    ball.home()  # bring the ball back to the centre of the screen (postision 0,0)
    ball.speed(1)
    ball.showturtle()


def goalieup():  # function to move golaie up.
    goalie.setheading(90)
    goalie.forward(5)


def goaliedown():  # function to move golaie down.
    goalie.setheading(270)
    goalie.forward(10)


def main():
    screen.onkeypress(goalieup, "Up")  # bind goalieup function to up arrow key.
    # When up arrow is pressed or held down the goalieup function is called.
    screen.onkeypress(goaliedown, "Down")  # bind goalie down to down arrow key
    screen.onkey(kick, " ")  # bind kick function to " " key.

    screen.listen()  # wait for a key to be pressed
    screen.mainloop()  # always have this as the last line of your turtle graphic program.


turtle.setup(1000, 600)
screen = turtle.Screen()

# Creating our turtles

goalie = turtle.Turtle()
ball = turtle.Turtle()

ball.penup()
ball.shape("circle")
ball.shapesize(2)
ball.fillcolor("orange")
ball.speed(1)
ball.setheading(180)

goalie = turtle.Turtle()
goalie.penup()
goalie.shape("turtle")
goalie.shapesize(2)
goalie.fillcolor("navy")
goalie.speed(10)
goalie.setheading(90)
goalie.goto(-300, 0)

main()
