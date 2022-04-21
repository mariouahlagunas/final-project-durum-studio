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
