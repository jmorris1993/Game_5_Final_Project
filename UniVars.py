# Tile size of the level
LEVEL_WIDTH = 50
LEVEL_HEIGHT = 50

CX = 25
CY = 25

# Tile size of the viewport (through which you view the level)
VIEWPORT_WIDTH = 31
VIEWPORT_HEIGHT = 31  

# Pixel size of a tile(which gives you the size of the window)
TILE_SIZE = 24

MOVE = {
    'Left': (-1,0),
    'Right': (1,0),
    'Up' : (0,-1),
    'Down' : (0,1)
}

EXITS = {
	'North' : 1,
	'East' : 2,
	'South' : 3,
	'West' : 4
}

# Pixel size of the viewport
WINDOW_WIDTH = TILE_SIZE * VIEWPORT_WIDTH
WINDOW_HEIGHT = TILE_SIZE * VIEWPORT_HEIGHT

# Pixel size of the panel on the right where you can display stuff
WINDOW_RIGHTPANEL = 0

PLAYER = 't_android_red.gif'
MONEY = 'money.gif'
MONEY5 = 'money5.gif'
MONEY50 = 'money50.gif'
GHOST = 'Ghost.gif'
ROBOT = 'bot.gif'
BALL = 'Ball.gif'
FIRFLO = 'FireFlower.gif'
KITTY = 'gegege-kitten.gif'
GAURD = 'Gaurd.gif'
SWORD = 'sword.gif'
SCORP = 'Scorpion.gif'
POTION = 'potion.gif'
STATUE = 'gray_bowser_statue.gif'
GRASS = 'grass-24.gif'
TREE = 'tree-24.gif'
HEALTH = 'HealthBar.gif'
DOOR_OPEN = 'Open_Door.gif'
DOOR_UP = 'door-closed_1.gif'
DOOR_DOWN = 'door-closed_3.gif'
DOOR_LEFT = 'door-closed_4.gif'
DOOR_RIGHT = 'door-closed_2.gif'
WALL = 'wall.gif'
WALL_GREEN = 'vine_wall.gif'
WALL_BLUE = 'wall_blue.gif'
WALL_YELLOW = 'wall_yellow.gif'
WALL_RED = 'wall_red.gif'
RED_ROCK = 'red_rock.gif'
YELLOW_ROCK = 'yellow_rock.gif'
BLUE_ROCK = 'ice_rock.gif'
BLACK_ROCK = 'bw_rock.gif'
RED_GRASS = 'grass-red.gif'
YELLOW_GRASS = 'grass-yellow.gif'
BLACK_GRASS = 'grass-bw.gif'
BLUE_GRASS = 'grass-ice.gif'

COLOR = {
	'RED' : ['red', 'red3', RED_GRASS, RED_ROCK, WALL_RED],
	'YELLOW' : ['orange', 'orange3', YELLOW_GRASS, YELLOW_ROCK, WALL_YELLOW],
	'BLUE' : ['cyan', 'blue', BLUE_GRASS, BLUE_ROCK, WALL_BLUE],
	'BLACK' : ['lightgrey', 'darkgrey', BLACK_GRASS, BLACK_ROCK, WALL],
	'GREEN' : ['lightgreen', 'green', GRASS, TREE, WALL_GREEN]
}