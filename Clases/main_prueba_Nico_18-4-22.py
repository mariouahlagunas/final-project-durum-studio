

# CLASE MAIN DE PRUEBA PERO SIN DISPARO, LO DEJO AQUI PARA PODER UTILIZAR DE ÉL EL MOVIMIENTO ACTUALIZADO

import arcade
import protagonista # Aquí se importa la clase de personaje

SCREEN_TITLE = "Juego de equipo Durum studio"
SPRITE_SCALING_PLAYER = 0.5
MOVEMENT_SPEED = 3

SPRITE_IMAGE_SIZE = 128
SPRITE_SIZE = int(SPRITE_IMAGE_SIZE * SPRITE_SCALING_PLAYER)

SCREEN_WIDTH = SPRITE_SIZE * 15
SCREEN_HEIGHT = SPRITE_SIZE * 10



class MyWindow(arcade.Window):
    """ Main Window """
    def __init__(self, width, height, title):
        """ Init """
        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.BLACK)
        self.personaje_principal = protagonista.Protagonista(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,0,0, ":resources:images/animated_characters/female_person/femalePerson_idle.png", SPRITE_SCALING_PLAYER, MOVEMENT_SPEED)

        # Track the current state of what key is pressed
        self.shift_pressed = False
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

    def setup(self):
        """ Set up everything """
        self.personaje_principal.setup()

    def update_player_speed(self):

        # Calculate speed based on the keys pressed
        self.personaje_principal.set_change_x(0)
        self.personaje_principal.set_change_y(0)

        velocidad_de_movimiento = self.personaje_principal.get_velocidad_de_movimiento()

        if self.up_pressed and not self.down_pressed:
            self.personaje_principal.set_change_y(velocidad_de_movimiento)
        elif self.down_pressed and not self.up_pressed:
            self.personaje_principal.set_change_y(-velocidad_de_movimiento)
        if self.left_pressed and not self.right_pressed:
            self.personaje_principal.set_change_x(-velocidad_de_movimiento)
        elif self.right_pressed and not self.left_pressed:
            self.personaje_principal.set_change_x(velocidad_de_movimiento)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.personaje_principal.draw()

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.personaje_principal.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        velocidad_de_movimiento = self.personaje_principal.get_velocidad_de_movimiento()
        if key == arcade.key.LSHIFT:
            self.shift_pressed = True
            self.personaje_principal.cambiar_velocidad_de_movimiento(2)
        if key == arcade.key.A:
            self.left_pressed = True
            self.update_player_speed()
        elif key == arcade.key.D:
            self.right_pressed = True
            self.update_player_speed()
        elif key == arcade.key.W:
            self.up_pressed = True
            self.update_player_speed()
        elif key == arcade.key.S:
            self.down_pressed = True
            self.update_player_speed()

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LSHIFT:
            self.shift_pressed = False
            self.personaje_principal.cambiar_velocidad_de_movimiento(0.5)
        if key == arcade.key.W:
            self.up_pressed = False
            self.update_player_speed()
        elif key == arcade.key.S:
            self.down_pressed = False
            self.update_player_speed()
        elif key == arcade.key.A:
            self.left_pressed = False
            self.update_player_speed()
        elif key == arcade.key.D:
            self.right_pressed = False
            self.update_player_speed()


def main():
    """ Main method """
    window = MyWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()