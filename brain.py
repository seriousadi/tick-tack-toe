import numpy as np
import pygame


class Brain:
    def __init__(self):
        self.tick_tack = [["00", "01", "02"], ["10", "11", "12"], ["20", "21", "22"]]
        self.marker_brain = True
        self.clicked_or_not_1d = []
        self.clicked_or_not_2d = []

    def checker(self):
        t_array = np.array(self.tick_tack). \
            transpose(). \
            tolist()  # making our list transpose and then converting it back to list
        arrays = [t_array, self.tick_tack]

        for n in arrays:
            # checking if 3 boxes are filled with same thing on a horizontal line
            for m in n:
                if m[0] == m[1] and m[1] == m[2]:
                    return True
            # checking if diagonal boxes are filled with the same thing
            if n[0][0] == n[1][1] and n[1][1] == n[2][2] or n[2][0] == n[1][1] and n[1][1] == n[0][2]:
                return True

    def add_mark(self, n, m, marker):
        self.tick_tack[n][m] = marker

    def handle_click(self, tick_tack_box):
        self.clicked_or_not_2d = []
        # when user clicks on a box it checks which one was clicked and appends true or false in
        # clicked_or_not based on that
        for n in tick_tack_box:
            self.clicked_or_not_2d.append(n.collidepoint(pygame.mouse.get_pos()))

        self.clicked_or_not_1d = self.clicked_or_not_2d
        # Making the clicked_or_not list into 2d list for future use
        self.clicked_or_not_2d = [self.clicked_or_not_2d[n - 3: n] for n in range(3, 10, 3)]

    def add_marker_brain(self,marker_type):
        # enumerating the clicked_or_not to get the index of the place clicked.
        for n, m in enumerate(self.clicked_or_not_2d):
            if True in m:
                self.add_mark(n, m.index(True), marker=marker_type)
