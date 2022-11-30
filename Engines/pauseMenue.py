# file -> setting -> install pygame package
import pygame
# pip install pygame-menu -U >>> in terminal
from menue_componenets.button import Button

WIDTH = 600
HEIGHT = 800
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 255))
pygame.display.flip()


# menue = pygame_menu.Menu("pause", 600, 400, theme=themes.THEME_BLUE)


def initilize():
    run = True
    while run:
        screen.fill((255, 255, 255))
        pygame.display.flip()
        event = pygame.event.get()
        for e in event:
            if e.type == pygame.QUIT:
                run = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    pause_menue()
                    pygame.display.update()


def create_pause_buttons():
    created_buttons = []
    cont = Button((20, 20, 100), WIDTH / 2 - 50, HEIGHT - 400, 100, 40, "continue")
    save = Button((20, 20, 100), WIDTH / 2 - 50, HEIGHT - 340, 100, 40, "save")
    runAway = Button((20, 20, 100), WIDTH / 2 - 50, HEIGHT - 280, 100, 40, "quit")
    created_buttons.append(cont)
    created_buttons.append(save)
    created_buttons.append(runAway)
    return created_buttons


def handle_event_in_pause_menue(event, pos, buttons):
    runM = True
    for e in event:
        if e.type == pygame.MOUSEBUTTONDOWN:
            if buttons[0].isOver(pos):
                runM = False
            if buttons[1].isOver(pos):
                # TODO : handle save function
                pass
            if buttons[2].isOver(pos):
                # TODO : handle quit function to quit game or return to start menue
                pass
        if e.type == pygame.MOUSEMOTION:
            for b in buttons:
                if b.isOver(pos):
                    b.color = (0, 255, 0)
                else:
                    b.color = (20, 20, 100)

    return runM


def pause_menue():
    buttons = create_pause_buttons()
    runMenue = True
    while runMenue:
        pos = pygame.mouse.get_pos()
        event = pygame.event.get()

        # handle events with current position
        runMenue = handle_event_in_pause_menue(event, pos, buttons)

        # draw buttons on the screen
        for b in buttons:
            b.draw(screen)

        pygame.display.update()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    initilize()
    pygame.quit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
