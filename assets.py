black_pearl = (28, 31, 32)
white = (255, 255, 255)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
orange = (255, 165, 0)

def get_color_by_value(value):
    if value == 1:
        return green
    elif value == 2:
        return red
    elif value == 3:
        return blue
    elif value == 4:
        return yellow
    elif value == 5:
        return cyan
    elif value == 6:
        return magenta
    elif value == 7:
        return orange
    
    return black_pearl