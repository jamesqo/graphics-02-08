from display import *

def draw_line(x0, y0, x1, y1, screen, color):
    dx = x1 - x0
    dy = y1 - y0
    if dx > 0 and dy > 0 and dy <= dx:
        # 1st octant
        draw_line_case1(x0, y0, x1, y1, dx, dy, screen, color)
    elif dx >= 0 and dy > 0 and dy > dx:
        # 2nd octant
        draw_line_case2(x0, y0, x1, y1, dx, dy, screen, color)
    elif dx < 0 and dy > 0 and dy >= -dx:
        # 3rd octant
        draw_line_case3(x0, y0, x1, y1, dx, dy, screen, color)
    else:
        draw_line_case4(x0, y0, x1, y1, dx, dy, screen, color)

def draw_line_case4(x0, y0, x1, y1, dx, dy, screen, color):
    a = dy
    b = -dx

    a_times_two = 2 * a
    b_times_two = 2 * b

    x, y = x0, y0
    indicator = -a_times_two + b # Testing (x - 1, y + 1/2)
    while x >= x1:
        plot(screen, color, x, y)
        if indicator < 0: # < 0 tests that point is below the line
            y += 1
            indicator += b_times_two
        x -= 1
        indicator -= a_times_two

def draw_line_case3(x0, y0, x1, y1, dx, dy, screen, color):
    # Since dx is negative in this case, the sign test for the indicator
    # function is flipped.
    # 0 > mx - y + b does not mean 0 > dy x - dx y + dx b.
    # Instead, indicator > 0 means the point is above the graph and
    # indicator < 0 means it's below.
    a = dy
    b = -dx

    a_times_two = 2 * a
    b_times_two = 2 * b

    x, y = x0, y0
    indicator = -a + b_times_two # Inputs to the indicator fn have changed.
                                 # We are testing (x - 1/2, y + 1) instead of (x + 1/2, y + 1) now.
                                 # Correspondingly, a is negated.
    while y <= y1:
        plot(screen, color, x, y)
        if indicator > 0:
            x -= 1
            indicator -= a_times_two
        y += 1
        indicator += b_times_two

def draw_line_case2(x0, y0, x1, y1, dx, dy, screen, color):
    a = dy
    b = -dx

    a_times_two = 2 * a
    b_times_two = 2 * b

    x, y = x0, y0
    indicator = a + b_times_two
    while y <= y1:
        plot(screen, color, x, y)
        if indicator < 0:
            x += 1
            indicator += a_times_two
        y += 1
        indicator += b_times_two

def draw_line_case1(x0, y0, x1, y1, dx, dy, screen, color):
    # y = mx + b
    # 0 = mx - y + b
    # 0 = dy * x - dx * y + dx * b
    a = dy
    b = -dx

    a_times_two = 2 * a
    b_times_two = 2 * b

    x, y = x0, y0
    indicator = a_times_two + b
    while x <= x1:
        plot(screen, color, x, y)
        if indicator > 0:
            y += 1
            indicator += b_times_two
        x += 1
        indicator += a_times_two
