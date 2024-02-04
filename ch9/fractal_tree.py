import random
import time
import turtle as t

t.tracer(1, 0)
t.setworldcoordinates(0, 0, 700, 700)
t.hideturtle()

def draw_branch(start_pos, direction, branch_len):
    print(branch_len)
    if branch_len < 5:
        return 
    
    t.penup()
    t.goto(start_pos)
    t.setheading(direction)

    t.pendown()
    t.pensize(max(branch_len / 7.0, 1))
    t.forward(branch_len)

    print(direction, LEFT_ANGLE, RIGHT_ANGLE)

    end_pos = t.position() # I guess this is to get the current pos of the turtle after we moved by the branch_len

    # structurally self-similar
    # left_dir = direction + LEFT_ANGLE
    # left_branch_len = branch_len - LEFT_DECREASE
    # right_dir = direction - RIGHT_ANGLE
    # right_branch_len = branch_len - RIGHT_DECREASE

    # diff values for each branch each call
    left_dir = direction + random.randint(10, 30)
    left_branch_len = branch_len - random.randint(8, 15)
    right_dir = direction - random.randint(10, 30)
    right_branch_len = branch_len - random.randint(8, 15)

    draw_branch(end_pos, left_dir, left_branch_len)
    draw_branch(end_pos, right_dir, right_branch_len)

seed = 0
while True:
    random.seed(seed)
    LEFT_ANGLE = random.randint(10, 30) 
    LEFT_DECREASE = random.randint(8, 15)
    RIGHT_ANGLE = random.randint(10, 30) 
    RIGHT_DECREASE = random.randint(8, 15)
    START_LEN = random.randint(80, 120)

    t.clear()
    t.penup()
    t.goto(10, 10)
    t.write('Seed: %s' % (seed))

    draw_branch((350, 10), 90, START_LEN)
    t.update()
    t.exitonclick()
    time.sleep(2)

    seed += 1 
