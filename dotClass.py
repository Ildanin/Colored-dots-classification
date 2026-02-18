import pygame as pg

class Dot:
    def __init__(self, screen, x: float, y: float, radius: float, color: tuple[int, int, int], border_width: int, border_color: tuple[int, int, int] = (255, 255, 255)) -> None:
        self.screen = screen
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.width = border_width
        self.border_color = border_color
        dots.append(self)
    
    def draw(self):
        pg.draw.circle(self.screen, self.color, 
                       (self.x, self.y), self.radius)
        pg.draw.circle(self.screen, self.border_color,
                       (self.x, self.y), self.radius, self.width)

dots: list[Dot] = []