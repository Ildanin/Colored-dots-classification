def generate_data(dots, width: int, height: int) -> tuple[list, list]:
    dataset = []
    answerset = []
    for dot in dots:
        dataset.append((dot.x / width, dot.y / height))
        answerset.append([factor/255 for factor in dot.color])
    return(dataset, answerset)

def rainbow_color(angle: float) -> tuple[int, int, int]:
    red = 0
    green = 0
    blue = 0
    if   0 <= angle <= 60:
        red = 255
        green = round(255 / 60 * angle)
        blue = 0
    elif 60 <= angle <= 120:
        red = round(255 - 255 / 60 * (angle - 60))
        green = 255
        blue = 0
    elif 120 <= angle <= 180:
        red = 0
        green = 255
        blue = round(255 / 60 * (angle - 120))
    elif 180 <= angle <= 240:
        red = 0
        green = round(255 - 255 / 60 * (angle - 180))
        blue = 255
    elif 240 <= angle <= 300:
        red = round(255 / 60 * (angle - 240))
        green = 0
        blue = 255
    elif 300 <= angle <= 360:
        red = 255
        green = 0
        blue = round(255 - 255 / 60 * (angle - 300))
    return((red, green, blue))