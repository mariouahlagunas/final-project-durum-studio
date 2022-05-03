import arcade

# Variables de la pantalla de juego
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1400
SCREEN_TITLE = "Juego de equipo Durum studio"

# Variables del protagonista
IMG_PROTAGONIST = ":resources:images/animated_characters/female_person/femalePerson_idle.png"
SCALE_PROTAGONIST = 0.5
HP_PROTAGONIST = 100
SPEED_PROTAGONIST = 5

# Variables de la barra de vida
HEALTHBAR_HEIGHT = 5
HEALTHBAR_WIDTH = 0.4

# Variables para las balas
IMG_BULLET_FIRE = ":resources:images/space_shooter/laserRed01.png"
SCALE_BULLET_FIRE = 2
DAMAGE_BULLET_FIRE = 20
SPEED_BULLET_FIRE = 10

IMG_BULLET_WATER = ":resources:images/space_shooter/laserBlue01.png"
SCALE_BULLET_WATER = 0.75
DAMAGE_BULLET_WATER = 10
SPEED_BULLET_WATER = 5

#Variable para escudo
IMG_ESCUDO = ":resources:images/items/coinGold.png"
SCALE_ESCUDO = 0.6

#Variables para setas
IMG_SETAS = ":resources:images/topdown_tanks/tank_green.png"
SCALE_SETAS = 0.8