import numpy as np

class Brain:
    def __int__(self):
        self.tick_tack = [["00", "01", "02"],
                          ["10", "11", "12"],
                          ["20", "21", "22"]]
        self.marker1 = "X"
        self.marker2 = "O"

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
