from display import *
from draw import *

if __name__ == '__main__':
    screen = new_screen()
    color = [0, 255, 0]

    # 1st octant
    draw_line(250, 250, 255 + 250, 81 + 250, screen, color)
    # 1st-2nd
    draw_line(250, 250, 255 + 250, 255 + 250, screen, color)
    # 2nd octant
    draw_line(250, 250, 255 + 250, 500 + 250, screen, color)
    # 2nd-3rd
    draw_line(250, 250, 250, 500 + 250, screen, color)
    # 3rd octant
    draw_line(250, 250, -250 + 250, 500 + 250, screen, color)
    # 3rd-4th octant
    draw_line(250, 250, -250 + 250, 250 + 250, screen, color)
    # 4th octant
    draw_line(250, 250, -250 + 250, 125 + 250, screen, color)
    # 4th-5th
    draw_line(250, 250, -250 + 250, 250, screen, color)
    # 5th octant
    draw_line(250, 250, -250 + 250, -125 + 250, screen, color)
    # 5th-6th
    draw_line(250, 250, -250 + 250, -250 + 250, screen, color)

    display(screen)
    save_extension(screen, 'img.png')
