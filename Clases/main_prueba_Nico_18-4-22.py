#CAMBIAR EL CÓDIGO TOTALMENTE A INGLÉS
                #LOS COMENTARIOS SERÁN EN ESPAÑOL
                #Clases en mayúsculas
                #Métodos en minúsculas.

import arcade

from Globals import *
from protagonista import *
from Bullet import *


class MyWindow(arcade.Window):

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.protagonist_list = None
        self.bullet_list = None

        self.protagonist = None

        # Track the current state of what key is pressed
        self.shift_pressed = False
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        self.camera_for_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_for_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)


    def setup(self):

        arcade.set_background_color(arcade.color.BLACK)

        self.protagonist_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        self.protagonist = Protagonista(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 0, 0)
        self.protagonist_list.append(self.protagonist)


    def on_draw(self):

        self.clear()
        arcade.start_render()

        self.camera_for_sprites.use()

        self.protagonist.draw()
        self.bullet_list.draw()

        self.camera_for_gui.use()

        arcade.draw_text(f"Health: {self.protagonist.get_hp()}", 10, 30, arcade.color.WHITE, 24)


    def on_update(self, delta_time):

        self.protagonist_list.update()
        self.bullet_list.update()

        for bullet in self.bullet_list:

            if bullet.bottom > self.height or bullet.top < 0 or bullet.right < 0 or bullet.left > self.width:
                bullet.remove_from_sprite_lists()


    def on_key_press(self, key, modifiers):

        if key == arcade.key.LSHIFT:
            self.shift_pressed = True
            self.protagonist_movement()
        if key == arcade.key.A:
            self.left_pressed = True
            self.protagonist_movement()
        elif key == arcade.key.D:
            self.right_pressed = True
            self.protagonist_movement()
        elif key == arcade.key.W:
            self.up_pressed = True
            self.protagonist_movement()
        elif key == arcade.key.S:
            self.down_pressed = True
            self.protagonist_movement()

        #Son solo para probar el tema de la vida (para eliminar)
        elif key == arcade.key.Q:
            self.protagonist.lose_life(5)
        elif key == arcade.key.E:
            self.protagonist.gain_life(5)


    def on_key_release(self, key, modifiers):

        if key == arcade.key.LSHIFT:
            self.shift_pressed = False
            self.protagonist_movement()
        if key == arcade.key.W:
            self.up_pressed = False
            self.protagonist_movement()
        elif key == arcade.key.S:
            self.down_pressed = False
            self.protagonist_movement()
        elif key == arcade.key.A:
            self.left_pressed = False
            self.protagonist_movement()
        elif key == arcade.key.D:
            self.right_pressed = False
            self.protagonist_movement()


    def on_mouse_press(self, x, y, button, modifiers):

        bullet = self.protagonist.shoot(x, y)
        self.bullet_list.append(bullet)


    def protagonist_movement(self):

        if self.shift_pressed:
            self.protagonist.change_movement_speed(1.5)
        else:
            self.protagonist.change_movement_speed(1)

        self.protagonist.not_move()
        if self.up_pressed and not self.down_pressed:
            self.protagonist.move_up()
        elif self.down_pressed and not self.up_pressed:
            self.protagonist.move_down()
        if self.left_pressed and not self.right_pressed:
            self.protagonist.move_left()
        elif self.right_pressed and not self.left_pressed:
            self.protagonist.move_right()


def main():
    window = MyWindow()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()