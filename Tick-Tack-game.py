import pygame
from brain import Brain
from ticktackboxmaker import TickTackBoxMaker, tick_tack_borders

# setting up Brain
brain = Brain()
marker_brain = brain.marker_brain
# make box
make_box = TickTackBoxMaker()

# pygame setup
pygame.init()
screen = pygame.display.set_mode((400, 500))
clock = pygame.time.Clock()
running = True

tick_tack_made = []

while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    tick_tack_box = make_box.tick_tack_box

    # making the border and boxes of the tick-tack board.
    make_box.make_tick_tack_box(screen=screen)  # This is also used as a click detector
    tick_tack_borders(screen=screen, box_border_color="white")

    left_mouse_click = pygame.mouse.get_pressed()[0]
    if left_mouse_click:
        brain.handle_click(tick_tack_box)  # handling click for board
        if True in brain.clicked_or_not_1d:
            # adding square cross mark
            add_mark_over = tick_tack_box[brain.clicked_or_not_1d.index(True)]
            width_half = add_mark_over.width / 2
            x_marker = add_mark_over.x + width_half
            y_marker = add_mark_over.y + width_half
            clk_box_loc_mark = (x_marker, y_marker, marker_brain)  # clicked box location and marker

            if (clk_box_loc_mark[0],clk_box_loc_mark[1]) not in [(n[0],n[1]) for n in tick_tack_made]:
                tick_tack_made.append(clk_box_loc_mark)
                marker_brain = not marker_brain
                brain.add_marker_brain(marker_brain)
                print(brain.tick_tack)

            won = brain.checker()  # check if someone won
            if won or len(tick_tack_made) == 9:
                running = False
                # flip() the display to put your work on screen

    for n in tick_tack_made:
        if n[2]:
            pygame.draw.circle(screen, "black", (n[0], n[1]), 40, 10)
        else:
            pygame.draw.rect(screen, "black", (n[0] - 30, n[1] - 30, 68, 68), 10)
    pygame.display.flip()

    clock.tick(10)  # limits FPS

pygame.quit()
