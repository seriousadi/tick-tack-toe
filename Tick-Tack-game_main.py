import pygame
from brain import Brain
from ticktackboxmaker import TickTackBoxMaker, tick_tack_borders
from time import sleep

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
# initializing font
default_font = pygame.font.get_default_font()
font = pygame.font.SysFont(default_font, size=50, bold=False, italic=False)
whose_turn = ""

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

            if (clk_box_loc_mark[0], clk_box_loc_mark[1]) not in [(n[0], n[1]) for n in tick_tack_made]:
                tick_tack_made.append(clk_box_loc_mark)
                marker_brain = not marker_brain
                brain.add_marker_brain(marker_brain)

            # check if someone won
            result = brain.checker()

            if result or len(tick_tack_made) == 9:
                won = result[0] if result else ""
                who_won = result[1] if result else ""

                # delaring Name of winner
                whose_turn = f"{'Square' if who_won else 'Circle'}" + " won" if not len(
                    tick_tack_made) == 9 else "It's a tie"

                running = False
                # flip() the display to put your work on screen

    # Turn Teller's logic
    img = font.render(whose_turn, True, "green")
    screen.blit(img, (95, 400))
    if marker_brain:
        whose_turn = "Circle's Turn"
    else:
        whose_turn = "Square's Turn"

    # This re-draws all the marks(circle,Square) on every frame
    for n in tick_tack_made:
        if n[2]:
            pygame.draw.circle(screen, "black", (n[0], n[1]), 40, 10)
        else:
            pygame.draw.rect(screen, "black", (n[0] - 30, n[1] - 30, 68, 68), 10)
    pygame.display.flip()

    clock.tick(10)  # limits FPS

    # Waiting For 3 Seconds before someone has won or tie
    if running == False:
        sleep(3)

pygame.quit()
