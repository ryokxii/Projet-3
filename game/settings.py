level_map = [
    "                            ",
    "                            ",
    "                            ",
    " XX    XXX            XX    ",
    " XX P                       ",
    " XXXX         XX         XX ",
    " XXXX       XX              ",
    " XX    X  XXXX    XX  XX    ",
    "       X  XXXX    XX  XXX   ",
    "    XXXX  XXXXXX  XX  XXXX  ",
    "XXXXXXXX  XXXXXX  XX  XXXX  ",
]
# 'X' : tile
# 'P' : Player spawn point
# add extra like coins, ennemies, etc

tile_size = 64
screen_width = 1200
screen_height = len(level_map) * tile_size

# game statuses
INTRO = 0
GUIDE = 1
ABOUT = 2
START = 3
WAITING = 4
GAME = 5
QUIT = 6
