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
    "enemigos": {"use_spatial_hash": True}
    }
# MAP_PATH = 'assets' + os.path.sep + 'tilemaps' + os.path.sep + 'PruebaMapaGrande3' + os.path.sep + 'mapaprueba3.tmx'
# MAP_SCALE = 1 ## DEVOLVERLO EL VALOR DE 1
# MAP_LAYER_OPTIONS = {
#     "suelo": {"use_spatial_hash": True},
#     "colisiones": {"use_spatial_hash": True},
#     "enemigos": {"use_spatial_hash": True},
#     "puerta": {"use_spatial_hash": True},
#     "decoracion": {"use_spatial_hash": True}
#     }



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

# Enemigo
TEXTURES_PATH_ENEMY = ":resources:images/animated_characters/female_person/femalePerson"
NUM_WALK_TEXTURES_ENEMY = 8
NUM_ATTACK_TEXTURES_ENEMY = 2
SCALE_ENEMY = 0.75
HP_ENEMY = 100
SPEED_ENEMY = 3

TIMER_FOR_UPDATE_IA = 0.5
DISTANCE_TO_ATTACK = 1000
TIME_FOR_SHOOT_MIN = 1
TIME_FOR_SHOOT_MAX = 3

#lskada
TEXTURES_PATH_MASCOTA = ":resources:images/animated_characters/female_person/femalePerson"
SCALE_MASCOTA = 0.5
SPEED_MASCOTA = 7
HP_MASCOTA = 75
NUM_WALK_TEXTURES_MASCOTA = 8




# VARIABLES DE LAS BALAS

# Balas genéricas
UPDATES_PER_FRAME_SHOOT = 10

# Balas de aire
TEXTURES_PATH_BULLET_AIR = 'assets' + os.path.sep + 'sprites' + os.path.sep + 'bullets' + os.path.sep + 'bullet_air' + os.path.sep
NUM_MOVE_TEXTURES_BULLET_AIR = 4
NUM_HIT_TEXTURES_BULLET_AIR = 4
TIME_MOVE_BULLET_AIR = 75
TIME_STOP_BULLET_AIR = 40
SCALE_BULLET_AIR = 0.2
DAMAGE_BULLET_AIR = 10
SPEED_BULLET_AIR = 5

# Balas de electricidad
TEXTURES_PATH_BULLET_ELECTRICITY = 'assets' + os.path.sep + 'sprites' + os.path.sep + 'bullets' + os.path.sep + 'bullet_electricity' + os.path.sep
NUM_MOVE_TEXTURES_BULLET_ELECTRICITY = 7
NUM_HIT_TEXTURES_BULLET_ELECTRICITY = 4
SCALE_BULLET_ELECTRICITY = 0.2
DAMAGE_BULLET_ELECTRICITY = 20
SPEED_BULLET_ELECTRICITY = 10

# Balas de agua
TEXTURES_PATH_BULLET_WATER = 'assets' + os.path.sep + 'sprites' + os.path.sep + 'bullets' + os.path.sep + 'bullet_water' + os.path.sep
NUM_MOVE_TEXTURES_BULLET_WATER = 6
NUM_TRANSACTION_TEXTURES_BULLET_WATER = 4
NUM_STOP_TEXTURES_BULLET_WATER = 7
TIME_MOVE_BULLET_WATER = 25
TIME_STOP_BULLET_WATER = 100
SCALE_BULLET_WATER = 0.1
DAMAGE_BULLET_WATER = 0.15
SPEED_BULLET_WATER = 5

# Balas de fuego
TEXTURES_PATH_BULLET_FIRE = 'assets' + os.path.sep + 'sprites' + os.path.sep + 'bullets' + os.path.sep + 'bullet_fire' + os.path.sep
NUM_MOVE_TEXTURES_BULLET_FIRE = 10
NUM_HIT_TEXTURES_BULLET_FIRE = 9
SCALE_BULLET_FIRE = 0.2
DAMAGE_BULLET_FIRE = 50
SPEED_BULLET_FIRE = 10
MAX_MULTIPLIER_TIMER_BULLET_FIRE = 3






#Variable para escudo
IMG_ESCUDO = ":resources:images/items/coinGold.png"
SCALE_ESCUDO = 0.6

#Variables para setas
IMG_SETAS = ":resources:images/topdown_tanks/tank_green.png"
SCALE_SETAS = 0.8

def xor(x, y):
    return bool((x and not y) or (not x and y))

DIFFICULTY = "hard"