import pygame as pg
from Button import Button
from settings import *


# this can either be the guide or about menu
class Other:
    def __init__(self, game, status, surface):
        self.game = game
        self.surface = surface

        back = Button("back", 20, 20, 100, 100)

        while self.game.status == status:
            self.surface.fill((0, 0, 0))

            for event in pg.event.get():
                pos = pg.mouse.get_pos()

                if event.type == pg.QUIT:
                    print("You quit in the middle of the game!")
                    self.game.running = False
                    quit()

                # mouse click
                if event.type == pg.MOUSEBUTTONDOWN:
                    if back.isOver(pos):
                        self.game.status = INTRO

                # mouse hover
                if event.type == pg.MOUSEMOTION:
                    back.isOver(pos)

            self.surface.blit(back.image, (back.x, back.y))

            pg.display.flip()
