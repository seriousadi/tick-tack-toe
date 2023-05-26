import pygame


class TickTackBoxMaker:
    def __init__(self):
        self.box_border_color = "white"
        self.tick_tack_box = []

    def make_tick_tack_box(self, screen):
        """this is used to draw boxes of tick-tack toe board of color red"""
        x_box = 40
        y_box = 40
        draw_squares = True
        self.tick_tack_box = []
        while draw_squares:

            if y_box > 256:
                draw_squares = False
            elif x_box > 256:
                y_box += 108
                x_box = 40
            else:
                rectangle = pygame.draw.rect(screen, "red", (x_box, y_box, 108, 108))
                self.tick_tack_box.append(rectangle)
                x_box += 108


def tick_tack_borders(screen, box_border_color):
    # Making boxes
    pygame.draw.rect(screen, box_border_color, (40, 40, 324, 324), width=5)
    pygame.draw.line(screen, box_border_color, (148, 40), (148, 360), width=3)
    pygame.draw.line(screen, box_border_color, (254, 40), (254, 360), width=3)
    pygame.draw.line(screen, box_border_color, (40, 148), (360, 148), width=3)
    pygame.draw.line(screen, box_border_color, (40, 254), (360, 254), width=3)
