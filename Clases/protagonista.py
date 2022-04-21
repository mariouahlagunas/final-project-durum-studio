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
import Balas
import math


class Protagonista(arcade.Sprite):

    def __init__(self, position_x, position_y, change_x, change_y, sprite, size, velocidad, hp):
        super().__init__()
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.player_sprite = arcade.Sprite(sprite, size)
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        self.hp_full = hp
        self.hp_now = hp

        self.velocidad_de_movimiento = velocidad

    def setup(self):
        self.player_sprite.center_x = self.position_x
        self.player_sprite.center_y = self.position_y

    def get_change_x(self, x):
        return self.change_x

    def set_change_x(self, x):
        self.change_x = x

    def get_change_y(self, y):
        return self.change_y

    def set_change_y(self, y):
        self.change_y = y

    def get_position_x(self):
        return self.player_sprite.center_x

    def set_position_x(self, x):
        self.player_sprite.center_x = x

    def get_position_y(self):
        return self.player_sprite.center_y

    def set_position_y(self, y):
        self.player_sprite.center_y = y

    def get_hpfull(self):
        return self.hp_full

    def get_hp(self):
        return self.hp_now

    def set_hp(self, new_hp):
        self.hp = new_hp

    def get_velocidad_de_movimiento(self):
        return self.velocidad_de_movimiento

    def set_velocidad_de_movimiento(self, velocidad_nueva):
        self.velocidad_de_movimiento = velocidad_nueva

    def cambiar_velocidad_de_movimiento(self, multiplicador):
        self.set_velocidad_de_movimiento(self.get_velocidad_de_movimiento() * multiplicador)

    def quitar_vida(self, cantidad):
        self.hp_now -= cantidad

    def imprimir_vida(self, width,HEALTHBAR_HEIGHT,cur_health,max_health):
        health_width = width * (cur_health /max_health)
        Bar_total= width * (max_health / max_health)
        if 0<cur_health<=max_health:
            arcade.draw_rectangle_filled(center_x=103 - 0.5 * (width - health_width),
                                         center_y=25 - 10,
                                         width=Bar_total + 10,
                                         height=HEALTHBAR_HEIGHT,
                                         color=arcade.color.RED)
            arcade.draw_rectangle_filled(center_x=103 - 0.5 * (width- health_width),
                                     center_y=25 - 10,
                                     width=health_width + 10,
                                     height=HEALTHBAR_HEIGHT,
                                     color=arcade.color.GREEN)


    def poner_vida(self, cantidad):
        self.hp_now += cantidad

    def disparar(self, start_x, start_y, end_x, end_y):
        # mirar con que arma se esta disparando
        # mirar si hay municion de esas arma en el inventario
        # en caso de que hay muncion, pues disparo
        bullet =Balas.Bala("laser", start_x, start_y)


        x_diff = end_x - start_x
        y_diff = end_y - start_y
        angle = math.atan2(y_diff, x_diff)
        bullet.angle = math.degrees(angle)
        print(f"Bullet angle: {bullet.angle:.2f}")
        bullet.change_x = math.cos(angle) * 10
        bullet.change_y = math.sin(angle) * 10
        return bullet

    def draw(self):
        """ Draw everything """
        self.player_list.draw()

    def update(self):
        self.player_sprite.center_y = self.player_sprite.center_y + self.change_y
        self.player_sprite.center_x = self.player_sprite.center_x + self.change_x
