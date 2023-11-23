import pygame
from tiles import Tile
from settings import tile_size, screen_width
from player import Player


class Level:
    def __init__(self, level_data, surface):
        # setup du level
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
        self.current_x = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if col == "X":  # creer les tiles + pos pour la map
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                elif col == "P":  # creer le player + pos dans la map
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width / 4 and direction_x < 0:  # bordure gauche
            self.world_shift = 8
            player.speed = 0
        elif (
            player_x > screen_width - (screen_width / 4) and direction_x > 0
        ):  # bordure droite
            self.world_shift = -8
            player.speed = 0
        else:  # interieur
            self.world_shift = 0
            player.speed = 8

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:  # mouvement de gauche
                    player.rect.left = sprite.rect.right
                    self.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:  # mouvement de droite
                    player.rect.right = sprite.rect.left
                    self.on_right = True
                    self.current_x = player.rect.right

            # check collision horizontale
        if player.on_left and (
            player.rect.left < self.current_x or player.direction.x >= 0
        ):
            player.on_left = False
        elif player.on_right and (
            player.rect.right > self.current_x or player.direction.x <= 0
        ):
            player.on_right = False

    def vertical_movement_collion(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:  # tomber
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:  # sauter
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceilling = True

            # check collision verticale
            if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
                player.on_ground = False
            elif player.on_ceilling and player.direction.y > 0:
                player.on_ceilling = False

    def run(self):
        # le level
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        # le joueur
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collion()
        self.player.draw(self.display_surface)
