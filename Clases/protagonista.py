# Clase personaje (Clase Padre, deciende de la clase sprite)
# Que tenga getters y setters.
# Getters de posicion.
# Movimiento (W.A.S.D para el protagoinsta, y para los demás personajes su IA)

# Ataque (un metodo de ataque)
# Vida (Puntos de vida, cambios de animaciones al ser golpeado?)


# Clase Protagonista (Clase hija)
# Que tenga getters y setters.
# Getters de posicion.
# Que herede el movimiento.
# Ataque - puede tener varios tipos de movimientos.

# Clase enemigo (Clase hija).
# Eso ya es para adelante.


# Para el lunes, pantalla vacia con un sprite que se mueva bien


# CLASE PROTAGONISTA ACTUALISADO PERO SIN DISPARO, LO DEJO AQUI PARA PODER UTILIZAR DE ÉL EL MOVIMIENTO ACTUALIZADO










import arcade

from Globals import *
from Bullet import *


class Protagonista(arcade.Sprite):

    def __init__(self, center_x, center_y, change_x, change_y):

        super().__init__(IMG_PROTAGONIST, SCALE_PROTAGONIST)

        self.center_x = center_x
        self.center_y = center_y
        self.change_x = change_x
        self.change_y = change_y

        self.movement_speed_normal = SPEED_PROTAGONIST
        self.movement_speed_now = SPEED_PROTAGONIST

        self.hp_max = HP_PROTAGONIST
        self.hp_now = HP_PROTAGONIST


    def draw(self):
        super()

        self.print_life()


    def change_movement_speed(self, multiplier):
        self.movement_speed_now = self.movement_speed_normal * multiplier


    def lose_life(self, amount):
        self.hp_now -= amount
        # Mirar el método en el que implementemos esto, ya que si la vida llega a 0 se pierde la partida.
        # Y depende de como se haga ese, ver como completamos este

    def gain_life(self, amount):
        self.hp_now += amount
        #Completar con el tema de que no se puede superar el hp_max nunca.


    def print_life(self):
        healthbar_height = HEALTHBAR_HEIGHT
        healthbar_height_framework = HEALTHBAR_HEIGHT + 4
        healthbar_width = HEALTHBAR_WIDTH * self.hp_now
        healthbar_width_framework = HEALTHBAR_WIDTH * self.hp_max + 4

        if self.hp_now > self.hp_max * 0.5:
            healthbar_color = arcade.color.GREEN
        elif self.hp_now > self.hp_max * 0.25:
            healthbar_color = arcade.color.YELLOW
        else:
            healthbar_color = arcade.color.RED
        healthbar_color_framework = arcade.color.BLACK

        arcade.draw_rectangle_filled(center_x = self.center_x,
                                     center_y = self.top + 5,
                                     width = healthbar_width_framework,
                                     height = healthbar_height_framework,
                                     color = healthbar_color_framework)

        arcade.draw_rectangle_filled(center_x = self.center_x - HEALTHBAR_WIDTH * 0.5 * (self.hp_max - self.hp_now),
                                     center_y = self.top + 5,
                                     width = healthbar_width,
                                     height = healthbar_height,
                                     color = healthbar_color)
        # Con lo que tenemos ahora mismo, en función de la vida maxima del personaje se imprime la barra.
        # Por lo que a más vida, la barra más grande. Y a menos vida, más pequeña.
        # Y si ponemos vidas diferentes, puede que quede raro


    def shoot(self, end_x, end_y):
        # Mirar con que arma se está disparando
        # Mirar potenciadores que pueda tener el personaje
        # Mirar si hay munición de esa arma en el inventario
        # En caso de que hay munición, pues disparo.
        # En caso contrario, alguna animación o mensaje de que no hay munición

        start_x = self.center_x
        start_y = self.center_y

        # Esto, obvio hay que hacerlo pillando el tipo de arma y los potenciadores que tenga el personaje
        type = "water"
        multiplier_scale = 1
        multiplier_damage = 1
        multiplier_speed = 1

        bullet = Bullet(start_x, start_y, end_x, end_y, type, multiplier_scale, multiplier_damage, multiplier_speed)

        return bullet












    def get_hp(self):
        return self.hp_now

    def get_change_x(self, x):
        return self.change_x

    def set_change_x(self, x):
        self.change_x = x

    def get_change_y(self, y):
        return self.change_y

    def set_change_y(self, y):
        self.change_y = y

    def get_hpfull(self):
        return self.hp_max

    def get_hp(self):
        return self.hp_now

    def set_hp(self, new_hp):
        self.hp = new_hp

    def get_velocidad_de_movimiento(self):
        return self.movement_speed_now

    def set_velocidad_de_movimiento(self, velocidad_nueva):
        self.velocidad_de_movimiento = velocidad_nueva