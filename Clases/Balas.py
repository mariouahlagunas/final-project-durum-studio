import random
import arcade
import math
import os


class Bala(arcade.Sprite):

    def __init__(self,tipo, start_x, start_y):
        if tipo=="laser":
            velocidad = 5
            scala = .5
            imagen =":resources:images/space_shooter/laserBlue01.png"
        elif tipo=="balin":
            velocidad = 5
            scala = .6
            imagen =":resources:images/space_shooter/laserBlue01.png"
        super().__init__(imagen, scala, center_x = start_x, center_y = start_y)

    def get_position_x(self):
        return self.center_x

    def set_position_x(self, x):
        self.center_x = x

    def get_position_y(self):
        return self.center_y

    def set_position_y(self, y):
        self.center_y = y