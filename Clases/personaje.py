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

import arcade


class Protagonista(arcade.Sprite):

    def __init__(self, position_x, position_y, change_x, change_y, sprite, size, velocidad):
        super().__init__()
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.player_sprite = arcade.Sprite(sprite, size)
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)
        self.hp = None
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

    def get_hp(self):
        return self.hp

    def set_hp(self, new_hp):
        self.hp = new_hp

    def get_velocidad_de_movimiento(self):
        return self.velocidad_de_movimiento

    def set_velocidad_de_movimiento(self, velocidad_nueva):
        self.velocidad_de_movimiento = velocidad_nueva

    def draw(self):
        """ Draw everything """
        self.player_list.draw()

    def update(self):
        self.player_sprite.center_y = self.player_sprite.center_y + self.change_y
        self.player_sprite.center_x = self.player_sprite.center_x + self.change_x
