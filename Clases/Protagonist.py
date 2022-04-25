# Clase personaje (Clase Padre, deciende de la clase sprite)
# Que tenga getters y setters.
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

        super().draw()

        self.print_life()


    def change_movement_speed(self, multiplier):
        self.movement_speed_now = self.movement_speed_normal * multiplier

    def not_move(self):
        self.change_x = 0
        self.change_y = 0

    def move_up(self):
        self.change_y = self.movement_speed_now

    def move_down(self):
        self.change_y = -self.movement_speed_now

    def move_left(self):
        self.change_x = -self.movement_speed_now

    def move_right(self):
        self.change_x = self.movement_speed_now


    def max_hp(self):
        return self.hp_max

    def now_hp(self):
        return self.hp_now

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