from display import *

def draw_line(x0, y0, x1, y1, screen, color):
    dx = x1 - x0
    dy = y1 - y0
    if dx > 0 and dy > 0 and dy <= dx:
        # 1st octant
        draw_line_case1(x0, y0, x1, y1, dx, dy, screen, color)
    else:
        draw_line_case2(x0, y0, x1, y1, dx, dy, screen, color)

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
        if indicator >= 0:
            y += 1
            indicator += b_times_two
        x += 1
        indicator += a_times_two
