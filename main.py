import numpy as np

tick_tack = [["00", "01", "02"],
             ["10", "11", "12"],
             ["20", "21", "22"]]


#
# marker = ["O", "X"]
# choose_marker = input("0 for (O ) or 1 for  (X) :")
#
#
#
# print(*tick_tack, sep='\n')
#
# game_on = True


def horizontal_checker():
    t_array = np.array(tick_tack).transpose()
    arrays = [t_array, tick_tack]
    for array in arrays:
        for row in array:
            if len(set(row)) == 1:
                print("me2")
                return True

        set_side = set([])
        for n in range(0, 3):
            set_side.add(array[n][n])

        if len(set_side) == 1:
            print("me")
            return True
        elif array[2][0] == array[0][2] and array[1][1] == array[2][0]:
            return True


game_on = True

while game_on:
    print(*tick_tack, sep="\n")
    if horizontal_checker():
        game_on = False

        print("You won the game yay")
    else:
        typer = input("where do you want to put your mark (Row/Column) : ").split('/')
        tick_tack[int(typer[0])][int(typer[1])] = "X"
