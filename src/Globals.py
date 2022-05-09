import arcade
import os



# VARIABLES DE LA PANTALLA DEL JUEGO

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1400
SCREEN_TITLE = "Juego de equipo Durum studio"



# VARIABLES DEL TILEDMAP

MAP_PATH = 'assets' + os.path.sep + 'tilemaps' + os.path.sep + 'pruebaMapa3' + os.path.sep + 'mapa3.tmx'
MAP_SCALE = 1
MAP_LAYER_OPTIONS = {
    "suelo": {"use_spatial_hash": True},
    "cajas": {"use_spatial_hash": True},
    "enemigos": {"use_spatial_hash": True, },
}



# VARIABLES DE LOS PERSONAJES

# Personaje generico
RIGHT_FACING = 0
LEFT_FACING = 1
UPDATES_PER_FRAME_WALK = 5
UPDATES_PER_FRAME_ATTACK = 10
HEALTHBAR_HEIGHT = 5
HEALTHBAR_WIDTH = 0.4

# Protagonista
TEXTURES_PATH_PROTAGONIST = ":resources:images/animated_characters/male_person/malePerson"
NUM_WALK_TEXTURES_PROTAGONIST = 8
NUM_ATTACK_TEXTURES_PROTAGONIST = 2
SCALE_PROTAGONIST = 0.75
HP_PROTAGONIST = 100
SPEED_PROTAGONIST = 5



# VARIABLES DE LAS BALAS

# Balas genericas
UPDATES_PER_FRAME_SHOOT = 5

# Balas de aire
TEXTURES_PATH_BULLET_AIR = 'assets' + os.path.sep + 'sprites' + os.path.sep + 'bullets' + os.path.sep + 'bullet_air'
NUM_MOVE_TEXTURES_BULLET_AIR = 6
NUM_NOT_MOVE_TEXTURES_BULLET_AIR = 6
SCALE_BULLET_AIR = 0.1
DAMAGE_BULLET_AIR = 5
SPEED_BULLET_AIR = 5
TIME_LIFE_MOVE_BULLET_AIR = 75
TIME_DEATH_MOVE_BULLET_AIR = 35

# Balas de electricidad
TEXTURES_PATH_BULLET_ELECTRICITY = 'assets' + os.path.sep + 'sprites' + os.path.sep + 'bullets' + os.path.sep + 'bullet_electricity'
NUM_MOVE_TEXTURES_BULLET_ELECTRICITY = 4
SCALE_BULLET_ELECTRICITY = 0.035
DAMAGE_BULLET_ELECTRICITY = 20
SPEED_BULLET_ELECTRICITY = 10

# Balas de agua
TEXTURES_PATH_BULLET_WATER = 'assets' + os.path.sep + 'sprites' + os.path.sep + 'bullets' + os.path.sep + 'bullet_water'
NUM_MOVE_TEXTURES_BULLET_WATER = 2
NUM_NOT_MOVE_TEXTURES_BULLET_WATER = 4
SCALE_BULLET_WATER = 0.1
DAMAGE_BULLET_WATER = 0.1
SPEED_BULLET_WATER = 5
TIME_LIFE_MOVE_BULLET_WATER = 50
TIME_DEATH_MOVE_BULLET_WATER = 100

# Balas de fuego
IMG_BULLET_FIRE = ":resources:images/space_shooter/laserRed01.png"
SCALE_BULLET_FIRE = 2
DAMAGE_BULLET_FIRE = 100
SPEED_BULLET_FIRE = 10






#Variable para escudo
IMG_ESCUDO = ":resources:images/items/coinGold.png"
SCALE_ESCUDO = 0.6

#Variables para setas
IMG_SETAS = ":resources:images/topdown_tanks/tank_green.png"
SCALE_SETAS = 0.8

<<<<<<< HEAD
#Variables de inventario
NUM_ESCUDOS = 2
NUM_SETAS = 2
NUM_FIRE = 30
NUM_WATER = 30
NUM_ELECTRICITY = 30
NUM_AIR = 30
NUM_MONEY = 100

=======
#xor
>>>>>>> 40b23bb498c08965ae064b083b58ff1f9d20a7e9
def xor(x, y):
    return bool((x and not y) or (not x and y))
