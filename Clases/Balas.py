import random
import arcade
import math
import os


class Bala(arcade.Sprite):

    def __init__(self,tipo, start_x, start_y, end_x, end_y):
        if tipo=="laser":
            velocidad = 5
            scala = .5
            imagen =":resources:images/space_shooter/laserBlue01.png"
        elif tipo=="balin":
            velocidad = 5
            scala = .6
            imagen =":resources:images/space_shooter/laserBlue01.png"

        super().__init__(imagen, scala)



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