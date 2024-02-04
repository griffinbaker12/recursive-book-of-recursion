import turtle as t
t.tracer(10000, 0)
t.setworldcoordinates(0, 0, 700, 700)
t.hideturtle()

MIN_SIZE = 6
DRAW_SOLID = True

def is_too_small(w, h):
    return w < MIN_SIZE or h < MIN_SIZE

def draw_inner_rectangles(x, y, w, h):
    if is_too_small(w, h):
        return 
    else:
        one_third_w = w / 3
        one_third_h = h / 3
        two_thirds_w = one_third_w * 2
        two_thirds_h = one_third_h * 2

        # move into position
        t.penup()
        t.goto(x + one_third_w, y + one_third_h)

        # draw inner rectangle first
        if DRAW_SOLID:
            t.fillcolor("white")
            t.begin_fill()
        t.pendown()
        t.goto(x + one_third_w, y + two_thirds_h)
        t.goto(x + two_thirds_w, y + two_thirds_h)
        t.goto(x + two_thirds_w, y + one_third_h)
        t.goto(x + one_third_w, y + one_third_h)
        t.penup()
        if DRAW_SOLID:
            t.end_fill()

        # draw inner rectangles across top
        draw_inner_rectangles(x, y + two_thirds_h, one_third_w, one_third_h)
        draw_inner_rectangles(x + one_third_w, y + two_thirds_h, one_third_w, one_third_h)
        draw_inner_rectangles(x + two_thirds_w, y + two_thirds_h, one_third_w, one_third_h)

        # # draw inner across middle (only 2 because we already hollowed out the middle)
        draw_inner_rectangles(x, y + one_third_h, one_third_w, one_third_h)
        draw_inner_rectangles(x + two_thirds_w, y + one_third_h, one_third_w, one_third_h)
        
        # draw inner across bottom
        draw_inner_rectangles(x, y, one_third_w, one_third_h)
        draw_inner_rectangles(x + one_third_w, y, one_third_w, one_third_h)
        draw_inner_rectangles(x + two_thirds_w, y, one_third_w, one_third_h)

def draw_carpet(x, y, w, h):
    # move pen into position
    t.penup()
    t.goto(x, y)

    # draw outer rectangle
    if DRAW_SOLID:
        t.fillcolor("black")
        t.begin_fill()
    t.goto(x, y+h)
    t.goto(x+w, y+h)
    t.goto(x+w, y)
    t.goto(x, y)
    if DRAW_SOLID:
        t.end_fill()
    t.penup()

    # draw inner rectangles
    draw_inner_rectangles(x, y, w, h)

draw_carpet(50, 50, 600, 600)

t.exitonclick()
