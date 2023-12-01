import sys
import pygame as pg

# move up one directory to be able to import the settings and images
sys.path.append("..")
from Button import Button
from settings import *


class Intro:
    def __init__(self, game, surface):
        self.game = game
        self.surface = surface
        start = Button("start", 400, 275, 300, 100)
        guide = Button("guide", 400, 400, 300, 100)
        about = Button("about", 400, 525, 300, 100)

        while self.game.status == INTRO:
            for event in pg.event.get():
                pos = pg.mouse.get_pos()

                if event.type == pg.QUIT:
                    print("You quit in the middle of the game!")
                    self.game.running = False
                    quit()

                # mouse click
                if event.type == pg.MOUSEBUTTONDOWN:
                    if start.isOver(pos):
                        # self.game.status = OVERWORLD
                        self.game.status = "overworld"
                    elif guide.isOver(pos):
                        self.game.status = GUIDE
                    elif about.isOver(pos):
                        self.game.status = ABOUT

                # mouse hover
                if event.type == pg.MOUSEMOTION:
                    start.isOver(pos)
                    guide.isOver(pos)
                    about.isOver(pos)

            self.surface.fill((0, 0, 0))
            self.surface.blit(start.image, (start.x, start.y))
            self.surface.blit(guide.image, (guide.x, guide.y))
            self.surface.blit(about.image, (about.x, about.y))

            pg.display.flip()
