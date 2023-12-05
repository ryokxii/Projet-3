import pygame as pg
from Button import Button
from settings import *


# this can either be the guide or about menu
class Other:
    def __init__(self, game, status, surface):
        self.game = game
        self.surface = surface

        back = Button("back", 20, 20, 100, 100)
        font = pg.font.Font(None, 42)
        checkbox_rect = pg.Rect(300, 300, 20, 20)
        checkbox_checked = True
        paused = False

        while self.game.status == status:
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
                    if checkbox_rect.collidepoint(event.pos):
                        checkbox_checked = not checkbox_checked
                        if checkbox_checked:
                            self.game.overworld_bg_music.play(loops=-1)
                            self.game.level_bg_music.play(loops=-1)
                        else:
                            self.game.overworld_bg_music.stop()
                            self.game.level_bg_music.stop()

                # mouse hover
                if event.type == pg.MOUSEMOTION:
                    back.isOver(pos)

            if status == GUIDE:
                guide_bg = pg.image.load(GUIDE_BG)
                self.surface.blit(guide_bg, ORIGIN)
            elif status == ABOUT:
                self.surface.fill("#D1AB9D")
                # Draw checkbox
                pg.draw.rect(self.surface, (0, 0, 0), checkbox_rect, 2)
                if checkbox_checked:
                    pg.draw.rect(
                        self.surface, (0, 255, 0), checkbox_rect.inflate(-4, -4)
                    )
                else:
                    pg.draw.rect(
                        self.surface, (255, 255, 255), checkbox_rect.inflate(-4, -4)
                    )

                # Draw text
                text = font.render(
                    "Music: " + ("On" if checkbox_checked else "Off"), True, (0, 0, 0)
                )
                self.surface.blit(text, (50, 300))

            self.surface.blit(back.image, (back.x, back.y))

            pg.display.flip()
