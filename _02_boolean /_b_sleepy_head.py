"""
Use boolean variables to control program logic between two different code
paths.
"""
import turtle


if __name__ == '__main__':
    my_turtle = turtle.Turtle()

    # TODO)
    #  1. Use a boolean variable to indicate if it is the weekend.
    #     Display a different message to the user depending on whether it is
    #     the weekend or not.
    #  2. Use a boolean variable to indicate if a student passed an exam.
    #     Display a different message to the user depending on whether they
    #     passed or not.
    #  3. Use a boolean variable to indicate if a game is over. When the game
    #     is over, tell the user.
    #  4. Use two boolean variables, one to indicate if a shape should be red,
    #     the other to indicate if the shape is to be square. When both
    #     variables are true, use a turtle to draw a red square.

    wekend=False
    if wekend == False:
        print('it is not the wekend')

    test=True
    if test == True:
        print('the studint passed the test')

    game=False
    if game == False:
        print('game over')

    shape_col_red=True
    if shape_col_red == True:
        window = turtle.Screen()
        window.bgcolor('white')
        my_turtle.shape("turtle")
        my_turtle.speed(2)
        my_turtle.color('green')
        my_turtle.pencolor('red')
        my_turtle.begin_fill()
        for i in range(4):
            my_turtle.forward(100)
            my_turtle.left(90)
        my_turtle.end_fill()

pass
