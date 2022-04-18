import random
import arcade
import math
import os
class Bala(arcade.Sprite):

    def __init__(self,x,y,BULLET_SPEED):
        super().__init__()
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        self.x = x
        self.y= y
        self.BULLET_SPEED=BULLET_SPEED
        self.bullet = arcade.Sprite(sprite, size)
        self.bullet_list = None
        self.gun_sound = arcade.sound.load_sound(":resources:sounds/laser1.wav")
        self.hit_sound = arcade.sound.load_sound(":resources:sounds/phaseJump1.wav")

        arcade.set_background_color(arcade.color.AMAZON)
    def get_change_x(self, x):
        return self.x
    def set_change_x(self, x):
        self.x = x
    def get_change_y(self, y):
        return self.y
    def set_change_y(self, y):
        self.y = y
    def get_BULLET_SPEED(self):
        return self.BULLET_SPEED

    def set_BULLET_SPEED(self, BULLET_SPEED):
        self.BULLET_SPEED = BULLET_SPEED


    def setup(self):

        """ Set up the game and initialize the variables. """
        self.bullet_list = arcade.SpriteList()

    def on_draw(self):
        self.bullet_list.draw()

    def on_update(self, delta_time):
        self.bullet_list.update()
        for bullet in self.bullet_list:
            if bullet.bottom > self.width or bullet.top < 0 or bullet.right < 0 or bullet.left > self.width:
                bullet.remove_from_sprite_lists()


def main():
    game = Bala()
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()