import random
import arcade
import math
import os


class Bala(arcade.Sprite):

    def __init__(self, tipo, start_x, start_y, end_x, end_y):
        if 1(tipo)
            velocidad = oqebtiowe
            scala = woubgow
            imagen = owbnegowe
            sonido
            de
            salida
            sonido
            de
            choque
        elif 2
            velocidad = oqebtiowe
            scala = woubgow
            imagen = owbnegowe

        super().__init__(img, scala)

        self.center_x = start_x
        self.center_y = start_y

        x_diff = end_x - start_x
        y_diff = end_y - start_y

        angle = math.atan2(y_diff, x_diff)
        self.angle = math.degrees(angle)

        bullet.change_x = math.cos(angle) * self.get_BULLET_SPEED()
        bullet.change_y = math.sin(angle) * self.get_BULLET_SPEED()

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