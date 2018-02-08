from display import *
from draw import *

if __name__ == '__main__':
    screen = new_screen()
    color = [0, 255, 0]

    display(screen)
    save_extension(screen, 'img.png')
