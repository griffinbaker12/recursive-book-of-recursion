import turtle as t
t.tracer(100, 0)
t.setworldcoordinates(0, 0, 700, 700)
t.hideturtle()
# once you are drawing triangles less than this h/w, we stop
MIN_SIZE = 4

def midpoint(start_x, start_y, end_x, end_y):
    x_diff = abs(start_x - end_x)
    y_diff = abs(start_y - end_y)
    return (min(start_x, end_x) + (x_diff/2), min(start_y, end_y) + (y_diff/2))

def is_too_small(ax, ay, bx, by, cx, cy):
    width = max(ax, bx, cx) - min(ax, bx, cx)
    height = max(ay, by, cy) - min(ay, by, cy)
    return width < MIN_SIZE or height < MIN_SIZE

def draw_triangle(ax, ay, bx, by, cx, cy):
    if is_too_small(ax, ay, bx, by, cx, cy):
        return
    else:
        t.penup()
        t.goto(ax, ay)
        t.pendown()
        t.goto(bx, by)
        t.goto(cx, cy)
        t.goto(ax, ay)
        t.penup()

        mid_ab = midpoint(ax, ay, bx, by)
        mid_bc = midpoint(bx, by, cx, cy)
        mid_ca = midpoint(cx, cy, ax, ay)

        draw_triangle(ax, ay, mid_ab[0], mid_ab[1], mid_ca[0], mid_ca[1])
        draw_triangle(mid_ab[0], mid_ab[1], bx, by, mid_bc[0], mid_bc[1])
        draw_triangle(mid_ca[0], mid_ca[1], mid_bc[0], mid_bc[1], cx, cy)
        return

draw_triangle(50, 50, 350, 650, 650, 50)

t.exitonclick()
