import turtle
import math

def draw_pythagoras_tree(t, branch_length, level):
    if level == 0:
        return

    # Draw the initial square
    for _ in range(4):
        t.forward(branch_length)
        t.right(90)

    # Position the turtle for the left branch
    t.forward(branch_length)
    t.left(45)

    # Calculate the length of the next branch
    next_branch_length = branch_length * math.sqrt(2) / 2

    # Draw the left branch
    draw_pythagoras_tree(t, next_branch_length, level - 1)

    # Position the turtle for the right branch
    t.right(90)
    draw_pythagoras_tree(t, next_branch_length, level - 1)

    # Move the turtle back to the original position
    t.left(45)
    t.forward(branch_length)
    t.right(90)
    t.forward(branch_length)
    t.right(90)

def main():
    level = int(input("Enter the level of recursion: "))

    screen = turtle.Screen()
    screen.title("Pythagoras Tree")

    t = turtle.Turtle()
    t.speed('fastest')
    t.penup()
    t.goto(-100, -100)
    t.pendown()

    draw_pythagoras_tree(t, 100, level)

    turtle.done()

if __name__ == "__main__":
    main()
