import turtle as t
t.tracer(0, 1000)
t.setworldcoordinates(0, 0, 700, 700)
t.hideturtle()
t.pensize(2)

def draw_koch_curve(start, heading, len):
    if len < 1:
        return
    else:
        # move to start
        recursive_args = []
        t.penup()
        t.goto(start)
        t.setheading(heading)
        recursive_args.append({ 'position': t.position(), 'heading': t.heading() })

        # erase middle third
        t.forward(len / 3)
        t.pencolor('white')
        t.pendown()
        t.forward(len / 3)

        # draw the bump
        t.backward(len / 3)
        t.left(60)
        recursive_args.append({ 'position': t.position(), 'heading': t.heading() })
        t.pencolor('black')
        t.forward(len / 3)
        t.right(120)
        recursive_args.append({ 'position': t.position(), 'heading': t.heading() })
        t.forward(len / 3)
        t.left(60)
        recursive_args.append({  'position': t.position(), 'heading': t.heading() })
        print(recursive_args, 'the args')

        # for each line, we draw 4 new ones
        # and for a line, you need:
        # 1) starting coord
        # 2) direction (heading)
        # 3) length
        for i in range(4):
            draw_koch_curve(recursive_args[i]['position'], recursive_args[i]['heading'], len / 3)

        return 

def draw_koch_flake(start, heading, len):
    t.penup()
    t.goto(start)
    t.setheading(heading)
    
    # create 4 starting lines, and then recursively divide them up
    for _ in range(4):
        # record starting pos and heading
        curve_starting_pos = t.position()
        curve_starting_heading = t.heading()
        draw_koch_curve(curve_starting_pos, curve_starting_heading, len)

        # move back to the start position for this side
        t.penup()
        t.goto(curve_starting_pos)
        t.setheading(curve_starting_heading)

        # move to the start pos of the next side
        t.forward(len)
        t.right(120)

draw_koch_flake((100, 500), 0, 500)
t.exitonclick()
